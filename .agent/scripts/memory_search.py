#!/usr/bin/env python3
"""
Memory Search Utility
Поиск по файлам памяти проекта
"""

import os
import re
import sys
from pathlib import Path
from typing import List, Dict, Tuple

# Путь к директории памяти
MEMORY_DIR = Path(__file__).parent.parent / "memory"


def search_in_file(file_path: Path, query: str) -> List[Tuple[int, str]]:
    """
    Ищет query в файле, возвращает список (номер_строки, строка)
    """
    results = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for i, line in enumerate(f, 1):
                if query.lower() in line.lower():
                    results.append((i, line.strip()))
    except Exception as e:
        print(f"Ошибка чтения {file_path}: {e}", file=sys.stderr)
    return results


def search_memory(query: str, categories: List[str] = None) -> Dict[str, List[Tuple[int, str]]]:
    """
    Ищет query во всех файлах памяти
    
    Args:
        query: Строка поиска
        categories: Список категорий для поиска (None = все)
    
    Returns:
        Словарь {путь_к_файлу: [(номер_строки, строка), ...]}
    """
    results = {}
    
    if not MEMORY_DIR.exists():
        print(f"Директория памяти не найдена: {MEMORY_DIR}", file=sys.stderr)
        return results
    
    # Определяем директории для поиска
    if categories:
        search_dirs = [MEMORY_DIR / cat for cat in categories if (MEMORY_DIR / cat).exists()]
    else:
        search_dirs = [d for d in MEMORY_DIR.iterdir() if d.is_dir()]
    
    # Ищем во всех .md файлах
    for dir_path in search_dirs:
        for file_path in dir_path.rglob("*.md"):
            file_results = search_in_file(file_path, query)
            if file_results:
                rel_path = file_path.relative_to(MEMORY_DIR.parent)
                results[str(rel_path)] = file_results
    
    return results


def format_results(results: Dict[str, List[Tuple[int, str]]], max_context: int = 100) -> str:
    """
    Форматирует результаты поиска для вывода
    """
    if not results:
        return "❌ Ничего не найдено"
    
    output = [f"📁 Найдено в {len(results)} файлах:\n"]
    
    for file_path, matches in results.items():
        output.append(f"\n**{file_path}**")
        for line_num, line in matches[:5]:  # Макс 5 совпадений на файл
            # Обрезаем длинные строки
            if len(line) > max_context:
                line = line[:max_context] + "..."
            output.append(f"  L{line_num}: {line}")
        
        if len(matches) > 5:
            output.append(f"  ... и ещё {len(matches) - 5} совпадений")
    
    return "\n".join(output)


def main():
    """
    CLI интерфейс
    """
    if len(sys.argv) < 2:
        print("Использование: python memory_search.py <запрос> [категория1,категория2,...]")
        print("\nПример:")
        print("  python memory_search.py 'PostgreSQL'")
        print("  python memory_search.py 'авторизация' 03_decisions,06_problems")
        sys.exit(1)
    
    query = sys.argv[1]
    categories = sys.argv[2].split(",") if len(sys.argv) > 2 else None
    
    print(f"🔍 Поиск: '{query}'")
    if categories:
        print(f"📂 Категории: {', '.join(categories)}")
    print()
    
    results = search_memory(query, categories)
    print(format_results(results))


if __name__ == "__main__":
    main()
