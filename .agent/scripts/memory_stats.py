#!/usr/bin/env python3
"""
Memory Stats Utility
Статистика системы памяти проекта
"""

import os
import sys
from pathlib import Path
from datetime import datetime
from typing import Dict, Tuple

# Путь к директории памяти
MEMORY_DIR = Path(__file__).parent.parent / "memory"


def get_category_stats(category_path: Path) -> Tuple[int, str, int]:
    """
    Получает статистику категории
    
    Returns:
        (количество_файлов, дата_последнего_обновления, размер_в_байтах)
    """
    if not category_path.exists():
        return (0, "—", 0)
    
    files = list(category_path.rglob("*.md"))
    # Исключаем _index.md и _template.md из подсчёта записей
    content_files = [f for f in files if not f.name.startswith("_")]
    
    if not files:
        return (0, "—", 0)
    
    # Находим самый новый файл
    latest_mtime = max(f.stat().st_mtime for f in files)
    latest_date = datetime.fromtimestamp(latest_mtime).strftime("%Y-%m-%d")
    
    # Считаем общий размер
    total_size = sum(f.stat().st_size for f in files)
    
    return (len(content_files), latest_date, total_size)


def get_memory_stats() -> Dict:
    """
    Собирает полную статистику памяти
    """
    stats = {
        "categories": {},
        "total_files": 0,
        "total_size": 0,
        "last_update": "—"
    }
    
    if not MEMORY_DIR.exists():
        return stats
    
    latest_mtime = 0
    
    # Получаем статистику по каждой категории
    for category_dir in sorted(MEMORY_DIR.iterdir()):
        if category_dir.is_dir():
            cat_name = category_dir.name
            files, last_update, size = get_category_stats(category_dir)
            
            stats["categories"][cat_name] = {
                "files": files,
                "last_update": last_update,
                "size": size
            }
            
            stats["total_files"] += files
            stats["total_size"] += size
            
            # Отслеживаем общую последнюю дату
            if category_dir.stat().st_mtime > latest_mtime:
                latest_mtime = category_dir.stat().st_mtime
    
    if latest_mtime > 0:
        stats["last_update"] = datetime.fromtimestamp(latest_mtime).strftime("%Y-%m-%d")
    
    return stats


def format_size(bytes_size: int) -> str:
    """
    Форматирует размер в читаемый вид
    """
    if bytes_size < 1024:
        return f"{bytes_size} B"
    elif bytes_size < 1024 * 1024:
        return f"{bytes_size / 1024:.1f} KB"
    else:
        return f"{bytes_size / (1024 * 1024):.1f} MB"


def print_stats(stats: Dict):
    """
    Выводит статистику в красивом формате
    """
    print("📊 СТАТИСТИКА ПАМЯТИ ПРОЕКТА")
    print("═" * 50)
    print()
    print("📁 Категории:")
    print()
    print(f"{'#':<4} {'Категория':<20} {'Записей':<10} {'Обновлено':<12} {'Размер':<10}")
    print("-" * 60)
    
    for i, (cat_name, cat_stats) in enumerate(stats["categories"].items(), 1):
        num = cat_name[:2] if cat_name[0].isdigit() else str(i)
        name = cat_name[3:] if cat_name[2] == "_" else cat_name
        print(f"{num:<4} {name:<20} {cat_stats['files']:<10} {cat_stats['last_update']:<12} {format_size(cat_stats['size']):<10}")
    
    print()
    print("═" * 50)
    print()
    print(f"📈 Итого записей: {stats['total_files']}")
    print(f"💾 Общий размер: {format_size(stats['total_size'])}")
    print(f"🕐 Последнее обновление: {stats['last_update']}")
    
    # Рекомендации
    print()
    print("📌 Рекомендации:")
    
    empty_categories = [
        name for name, s in stats["categories"].items() 
        if s["files"] == 0
    ]
    
    if empty_categories:
        print(f"   • Заполни пустые категории: {', '.join(empty_categories[:3])}")
    
    if stats["total_files"] < 5:
        print("   • Добавь больше записей для эффективной работы памяти")
    
    if stats["total_files"] > 50:
        print("   • Проверь актуальность старых записей")


def main():
    """
    CLI интерфейс
    """
    stats = get_memory_stats()
    print_stats(stats)


if __name__ == "__main__":
    main()
