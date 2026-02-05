const fs = require('fs');
const path = require('path');

// --- НАСТРОЙКИ: ЧТО ИГНОРИРОВАТЬ ---
// Сюда добавляем папки, которые НЕ нужны AI (мусор, сборка, зависимости)
const IGNORE_DIRS = [
    'node_modules',
    '.git',
    '.vscode',
    '.idea',
    'dist',
    'build',
    '.next',
    'coverage',
    '__pycache__'
];

// Сюда добавляем расширения файлов, которые не важны для структуры (картинки, локи)
const IGNORE_EXTENSIONS = [
    '.png', '.jpg', '.jpeg', '.svg', '.ico', 
    '.lock', '-lock.json', '.log', '.map'
];

function getTree(dir, prefix = '') {
    let output = '';
    
    // Читаем содержимое папки
    let items;
    try {
        items = fs.readdirSync(dir);
    } catch (e) {
        return ''; // Если нет прав доступа
    }

    // Фильтруем (убираем игнорируемое)
    items = items.filter(item => {
        // Пропускаем скрытые файлы (начинаются с точки), кроме .env.example если нужно
        if (item.startsWith('.') && item !== '.env.example') return false; 
        if (IGNORE_DIRS.includes(item)) return false;
        
        // Проверяем расширения для файлов
        if (fs.statSync(path.join(dir, item)).isFile()) {
            const ext = path.extname(item).toLowerCase();
            if (IGNORE_EXTENSIONS.includes(ext)) return false;
        }
        return true;
    });

    // Сортируем: Папки сверху, файлы снизу
    items.sort((a, b) => {
        const aPath = path.join(dir, a);
        const bPath = path.join(dir, b);
        const aIsDir = fs.statSync(aPath).isDirectory();
        const bIsDir = fs.statSync(bPath).isDirectory();
        
        if (aIsDir && !bIsDir) return -1;
        if (!aIsDir && bIsDir) return 1;
        return a.localeCompare(b);
    });

    // Строим дерево
    items.forEach((item, index) => {
        const isLast = index === items.length - 1;
        const pointer = isLast ? '└── ' : '├── ';
        const itemPath = path.join(dir, item);
        
        output += `${prefix}${pointer}${item}\n`;

        if (fs.statSync(itemPath).isDirectory()) {
            const newPrefix = prefix + (isLast ? '    ' : '│   ');
            output += getTree(itemPath, newPrefix);
        }
    });

    return output;
}

// Запуск
console.log('--- PROJECT STRUCTURE START ---');
console.log('.');
console.log(getTree(process.cwd())); // Сканирует текущую папку
console.log('--- PROJECT STRUCTURE END ---');