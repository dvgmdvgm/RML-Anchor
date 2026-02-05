#!/usr/bin/env python3
"""
Memory Validate Utility
Валидация структуры системы памяти
"""

import os
import sys
from pathlib import Path
from typing import List, Tuple

# Путь к директории памяти
AGENT_DIR = Path(__file__).parent.parent
MEMORY_DIR = AGENT_DIR / "memory"

# Ожидаемая структура
EXPECTED_CATEGORIES = [
    "01_project",
    "02_architecture", 
    "03_decisions",
    "04_domain",
    "05_code",
    "06_problems",
    "07_context",
    "08_people",
    "09_external",
    "10_testing",
    "11_deployment",
    "12_roadmap",
    "13_preferences"
]

EXPECTED_FILES = {
    "root": [
        "MEMORY_INDEX.md"
    ],
    "skills": [
        "MEMORY_SKILL.md"
    ],
    "workflows": [
        "remember.md",
        "recall.md",
        "start-session.md",
        "end-session.md",
        "memory-stats.md"
    ]
}


def validate_structure() -> Tuple[List[str], List[str]]:
    """
    Проверяет структуру системы памяти
    
    Returns:
        (список_ошибок, список_предупреждений)
    """
    errors = []
    warnings = []
    
    # Проверяем главные файлы
    if not (AGENT_DIR / "MEMORY_INDEX.md").exists():
        errors.append("❌ Отсутствует MEMORY_INDEX.md")
    
    # Проверяем skills
    skill_file = AGENT_DIR / "skills" / "MEMORY_SKILL.md"
    if not skill_file.exists():
        errors.append("❌ Отсутствует skills/MEMORY_SKILL.md")
    
    # Проверяем workflows
    for workflow in EXPECTED_FILES["workflows"]:
        workflow_file = AGENT_DIR / "workflows" / workflow
        if not workflow_file.exists():
            warnings.append(f"⚠️ Отсутствует workflow: {workflow}")
    
    # Проверяем директорию памяти
    if not MEMORY_DIR.exists():
        errors.append("❌ Отсутствует директория memory/")
        return errors, warnings
    
    # Проверяем категории
    for category in EXPECTED_CATEGORIES:
        cat_path = MEMORY_DIR / category
        
        if not cat_path.exists():
            errors.append(f"❌ Отсутствует категория: {category}/")
            continue
        
        # Проверяем наличие _index.md
        index_file = cat_path / "_index.md"
        if not index_file.exists():
            errors.append(f"❌ Отсутствует {category}/_index.md")
    
    # Проверяем наличие шаблонов для decisions и problems
    for category in ["03_decisions", "06_problems"]:
        template_file = MEMORY_DIR / category / "_template.md"
        if not template_file.exists():
            warnings.append(f"⚠️ Отсутствует шаблон: {category}/_template.md")
    
    # Проверяем context подпапки
    context_dir = MEMORY_DIR / "07_context"
    if context_dir.exists():
        session_history = context_dir / "session_history"
        if not session_history.exists():
            warnings.append("⚠️ Отсутствует 07_context/session_history/")
    
    return errors, warnings


def print_validation_result(errors: List[str], warnings: List[str]):
    """
    Выводит результат валидации
    """
    print("🔍 ВАЛИДАЦИЯ СИСТЕМЫ ПАМЯТИ")
    print("═" * 50)
    print()
    
    if not errors and not warnings:
        print("✅ Всё в порядке! Структура памяти корректна.")
        return
    
    if errors:
        print("❌ ОШИБКИ (требуют исправления):")
        for error in errors:
            print(f"   {error}")
        print()
    
    if warnings:
        print("⚠️ ПРЕДУПРЕЖДЕНИЯ:")
        for warning in warnings:
            print(f"   {warning}")
        print()
    
    print("═" * 50)
    print(f"Итого: {len(errors)} ошибок, {len(warnings)} предупреждений")
    
    if errors:
        print("\n💡 Запусти создание недостающих файлов или исправь вручную.")


def main():
    """
    CLI интерфейс
    """
    errors, warnings = validate_structure()
    print_validation_result(errors, warnings)
    
    # Возвращаем код ошибки если есть проблемы
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
