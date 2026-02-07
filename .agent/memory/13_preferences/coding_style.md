# 💻 Coding Style Preferences — Full Reference

> **Read this file to maintain consistent code style across all AI models.**
> **Читай этот файл для сохранения единого стиля кода между всеми AI моделями.**
>
> Based on Claude Opus 4.5/4.6 (Extended Thinking) coding patterns.
> Covers: Python, JavaScript/TypeScript, React, Java, Rust, Go, C++, C#, HTML/CSS, SQL, Django Templates.
>
> **AI: How to edit this file:**
> - To update an existing rule → find the correct section by its header (`## 🐍 Python`, `## 💜 C#`, etc.) and edit within that section
> - To add a new language/framework → create a new `## ` section following the same structure as existing ones, place it **before** the `🔀 Language Comparison` table, and add the language to that comparison table
> - **Never** append loose rules to the end of the file — always use structured sections

---

## 📐 General Philosophy

1. **Explicit > Implicit** — Clear code over clever code
2. **DRY** — Don't Repeat Yourself
3. **KISS** — Keep It Simple, Stupid
4. **YAGNI** — You Aren't Gonna Need It
5. **Single Responsibility** — One function = one purpose
6. **Defensive Programming** — Validate inputs, handle edge cases
7. **Descriptive Naming** — Full words, no abbreviations (`user_name` not `un`)
8. **Comments explain WHY, not WHAT** — Code should be self-documenting

### Naming Anti-patterns (All Languages)

| ❌ Never | ✅ Always |
|----------|-----------|
| `d` | `user_data` |
| `fn` | `calculate_total` |
| `cb` | `on_click_handler` |
| `idx` | `user_index` |
| `tmp` | `cached_response` |
| `e` | `error` / `exception` |
| `res` | `response` |
| `req` | `request` |

### Comments (All Languages)

```
# Single line: Brief explanation

# Multi-line:
# Longer explanation that spans
# multiple lines for clarity

# TODO: Description of what needs to be done
# FIXME: Description of what's broken
# NOTE: Important information
# HACK: Temporary workaround
```

### File Structure Order (All Languages)

```
1. Imports / dependencies
2. Constants / configuration
3. Types / interfaces / models
4. Helper functions (private)
5. Main logic (public API)
6. Entry point / exports
```

### Test Structure (All Languages)

```
Arrange → Act → Assert
```

---

## 🐍 Python

### Formatting

```
INDENTATION=4 spaces
LINE_LENGTH=100
QUOTES=double (")
PYTHON_VERSION=3.10+
LINTER=ruff
TYPE_CHECKER=mypy
```

### Naming Conventions

| Element | Style | Example |
|---------|-------|---------|
| Variables | snake_case | `user_name`, `total_count` |
| Functions | snake_case | `get_user()`, `calculate_total()` |
| Classes | PascalCase | `UserProfile`, `OrderManager` |
| Constants | UPPER_SNAKE | `MAX_RETRIES`, `API_URL` |
| Private | _prefix | `_internal_method()` |
| Type aliases | PascalCase | `UserDict`, `Callback` |

### Type Hints — ALWAYS

```python
from typing import Optional

def find_user(
    user_id: int,
    include_deleted: bool = False,
) -> Optional[User]:
    """Find user by ID with optional include of soft-deleted users."""
    ...
```

### Docstrings (Google Style)

```python
def process_payment(
    amount: Decimal,
    currency: str,
    customer_id: int,
) -> PaymentResult:
    """Process a payment for the given customer.

    Args:
        amount: Payment amount as Decimal. Must be positive.
        currency: ISO 4217 currency code (e.g., "USD", "EUR").
        customer_id: ID of the customer making the payment.

    Returns:
        PaymentResult with transaction ID and status.

    Raises:
        InsufficientFundsError: If customer balance is too low.
        InvalidCurrencyError: If currency code is not supported.
    """
```

### Imports Order

```python
# 1. Standard library
import os
import sys
from pathlib import Path
from datetime import datetime, timedelta

# 2. Third-party
import requests
from sqlalchemy import Column, Integer, String
from flask import Flask, request, jsonify

# 3. Local
from app.models import User, Payment
from app.utils.validators import validate_email
from app.config import settings
```

### Preferred Patterns

```python
# ✅ f-strings
message = f"Hello, {user.name}! You have {count} notifications."

# ✅ Comprehensions (when simple)
active_emails = [u.email for u in users if u.is_active]

# ✅ Context managers
with open(filepath, "r", encoding="utf-8") as f:
    data = json.load(f)

# ✅ dataclasses (Python 3.10+)
from dataclasses import dataclass

@dataclass
class UserProfile:
    name: str
    email: str
    age: int
    is_verified: bool = False

# ✅ match/case (Python 3.10+)
match status_code:
    case 200:
        return parse_response(data)
    case 404:
        raise NotFoundError(url)
    case _:
        raise UnexpectedStatusError(status_code)

# ✅ Enum instead of magic strings
from enum import Enum

class OrderStatus(Enum):
    PENDING = "pending"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

# ✅ Walrus operator when appropriate
if (match := pattern.search(text)) is not None:
    process(match.group(1))
```

### Error Handling

```python
# ✅ Specific exceptions, not bare except
try:
    user = await db.get_user(user_id)
except UserNotFoundError:
    logger.warning(f"User {user_id} not found")
    return ErrorResponse(404, "User not found")
except Exception as e:
    logger.exception(f"Unexpected error: {e}")
    return ErrorResponse(500, "Internal server error")
```

---

## 🌐 JavaScript / TypeScript

### Formatting

```
INDENTATION=2 spaces
QUOTES=single (')
SEMICOLONS=yes
MODULE_SYSTEM=ES modules (import/export)
```

### Naming Conventions

| Element | Style | Example |
|---------|-------|---------|
| Variables | camelCase | `userName`, `totalCount` |
| Functions | camelCase | `getUser()`, `calculateTotal()` |
| Classes | PascalCase | `UserProfile`, `OrderManager` |
| Interfaces | PascalCase | `UserProfile`, `CreateOrderRequest` |
| Type aliases | PascalCase | `OrderStatus`, `ApiResult` |
| Constants | UPPER_SNAKE | `MAX_RETRIES`, `API_URL` |
| Components (React) | PascalCase | `UserCard`, `NavBar` |
| Files | kebab-case | `user-profile.ts`, `order-status.ts` |
| Booleans | semantic prefix | `isActive`, `hasPermission`, `canEdit` |
| Generics | T prefix | `TValue`, `TResult`, `TEntity` |

### TypeScript — Type-First Design

```typescript
// ✅ Interfaces for object shapes
interface CreateUserRequest {
  readonly name: string;
  readonly email: string;
  readonly role: UserRole;
  readonly metadata?: Record<string, unknown>;
}

// ✅ Discriminated unions
type ApiResult<T> =
  | { success: true; data: T }
  | { success: false; error: string; code: number };

// ✅ Branded types for primitives
type UserId = string & { readonly __brand: 'UserId' };
type Email = string & { readonly __brand: 'Email' };

// ✅ satisfies instead of as
const config = {
  port: 3000,
  host: 'localhost',
} satisfies ServerConfig;

// ✅ Type guards
function isUser(value: unknown): value is User {
  return typeof value === 'object' && value !== null && 'id' in value;
}

// ✅ Exhaustive switch
function getStatusLabel(status: OrderStatus): string {
  switch (status) {
    case 'pending': return 'Pending';
    case 'completed': return 'Completed';
    default: {
      const _exhaustive: never = status;
      throw new Error(`Unknown status: ${_exhaustive}`);
    }
  }
}
```

### Async/Await

```typescript
// ✅ async/await over .then() chains
async function fetchUserProfile(userId: string): Promise<UserProfile> {
  const response = await fetch(`/api/users/${userId}`);
  if (!response.ok) {
    throw new ApiError(`Failed to fetch user: ${response.status}`);
  }
  return response.json();
}

// ✅ Parallel requests
const [user, orders, notifications] = await Promise.all([
  fetchUser(userId),
  fetchOrders(userId),
  fetchNotifications(userId),
]);
```

### Functions

```javascript
// ✅ Arrow functions for callbacks
const items = data.map((item) => item.name);

// ✅ Named functions for exports
export function getUserById(id) {
  // ...
}
```

---

## ⚛️ React (JSX/TSX)

### Component Style

```tsx
// ✅ Functional components + hooks, NEVER class components
interface UserCardProps {
  readonly user: User;
  readonly onEdit?: (userId: string) => void;
  readonly variant?: 'compact' | 'full';
}

export function UserCard({ user, onEdit, variant = 'full' }: UserCardProps) {
  const [isExpanded, setIsExpanded] = useState(false);

  const handleEdit = useCallback(() => {
    onEdit?.(user.id);
  }, [onEdit, user.id]);

  return (
    <div className="user-card">
      <h3>{user.name}</h3>
      {onEdit && (
        <button onClick={handleEdit} type="button">Edit</button>
      )}
    </div>
  );
}

// ✅ Custom hooks with use prefix
function useDebounce<T>(value: T, delay: number): T {
  const [debouncedValue, setDebouncedValue] = useState(value);

  useEffect(() => {
    const timer = setTimeout(() => setDebouncedValue(value), delay);
    return () => clearTimeout(timer);
  }, [value, delay]);

  return debouncedValue;
}
```

---

## ☕ Java

### Formatting

```
INDENTATION=4 spaces
LINE_LENGTH=120
BRACES=same line (K&R)
```

### Naming Conventions

| Element | Style | Example |
|---------|-------|---------|
| Variables | camelCase | `userName`, `orderCount` |
| Methods | camelCase | `getUser()`, `processPayment()` |
| Classes | PascalCase | `PaymentService`, `UserRepository` |
| Constants | UPPER_SNAKE | `MAX_RETRIES`, `DEFAULT_TIMEOUT` |
| Packages | lowercase | `com.example.service` |

### Class Structure

```java
public class PaymentService {
    
    private static final Logger logger = LoggerFactory.getLogger(PaymentService.class);
    private static final int MAX_RETRY_ATTEMPTS = 3;
    
    private final PaymentGateway gateway;
    private final UserRepository userRepository;
    
    // ✅ Constructor injection (NEVER field injection)
    public PaymentService(PaymentGateway gateway, UserRepository userRepository) {
        this.gateway = Objects.requireNonNull(gateway, "gateway must not be null");
        this.userRepository = Objects.requireNonNull(userRepository);
    }
    
    /**
     * Processes a payment for the specified user.
     *
     * @param userId the ID of the user
     * @param amount the payment amount (must be positive)
     * @return the payment result
     * @throws UserNotFoundException if the user does not exist
     */
    public PaymentResult processPayment(long userId, BigDecimal amount) {
        if (amount.compareTo(BigDecimal.ZERO) <= 0) {
            throw new IllegalArgumentException("Amount must be positive: " + amount);
        }
        
        User user = userRepository.findById(userId)
                .orElseThrow(() -> new UserNotFoundException(userId));
        
        return gateway.charge(user.getPaymentMethod(), amount);
    }
}
```

### Modern Java Patterns

```java
// ✅ Records for DTOs (Java 16+)
public record CreateUserRequest(String name, String email, UserRole role) {
    public CreateUserRequest {
        Objects.requireNonNull(name, "name must not be null");
        if (name.isBlank()) throw new IllegalArgumentException("name must not be blank");
    }
}

// ✅ Sealed interfaces (Java 17+)
public sealed interface Shape permits Circle, Rectangle, Triangle {
    double area();
}

// ✅ Optional instead of null
public Optional<User> findByEmail(String email) {
    return Optional.ofNullable(entityManager.find(User.class, email));
}

// ✅ Stream API (don't overuse)
List<String> activeEmails = users.stream()
        .filter(User::isActive)
        .map(User::getEmail)
        .sorted()
        .toList();
```

---

## 🦀 Rust

### Naming Conventions

| Element | Style | Example |
|---------|-------|---------|
| Variables | snake_case | `user_name`, `total_count` |
| Functions | snake_case | `get_user()`, `calculate_total()` |
| Types/Structs | PascalCase | `UserProfile`, `NetworkPacket` |
| Constants | UPPER_SNAKE | `MAX_RETRIES`, `DEFAULT_PORT` |
| Traits | PascalCase | `Serialize`, `Display` |
| Modules | snake_case | `user_service`, `network` |
| Crates | snake_case | `my_crate` |

### Idioms

```rust
// ✅ Ownership and borrowing — pass references when possible
pub fn print_name(name: &str) {
    println!("Hello, {name}");
}

// ✅ impl Into for flexible constructors
impl UserProfile {
    pub fn new(name: impl Into<String>, email: impl Into<String>) -> Result<Self, ValidationError> {
        let email = email.into();
        if !email.contains('@') {
            return Err(ValidationError::InvalidEmail(email));
        }
        Ok(Self { name: name.into(), email, created_at: Utc::now() })
    }
}

// ✅ thiserror for custom errors
#[derive(Debug, thiserror::Error)]
pub enum AppError {
    #[error("User not found: {0}")]
    UserNotFound(UserId),
    #[error("Database error: {0}")]
    Database(#[from] sqlx::Error),
}

// ✅ ? operator, NEVER .unwrap() in production
async fn fetch_data(url: &str) -> Result<Data, AppError> {
    let response = reqwest::get(url).await?;
    let data: Data = response.json().await?;
    Ok(data)
}

// ✅ Exhaustive pattern matching
fn process_command(cmd: Command) -> Result<(), AppError> {
    match cmd {
        Command::Create { name, email } => create_user(&name, &email),
        Command::Delete { id } => delete_user(id),
        Command::Update { id, fields } => update_user(id, &fields),
    }
}

// ✅ Iterator chains
let active_count = users.iter()
    .filter(|u| u.is_active())
    .filter(|u| u.last_login() > cutoff_date)
    .count();

// ✅ Derive common traits
#[derive(Debug, Clone, PartialEq, Eq, Hash, Serialize, Deserialize)]
pub struct UserId(String);
```

---

## 🐹 Go

### Naming Conventions

| Element | Style | Example |
|---------|-------|---------|
| Private | camelCase | `userName`, `getUser()` |
| Public | PascalCase | `UserName`, `GetUser()` |
| Packages | lowercase | `user`, `httputil` |
| Interfaces | PascalCase, -er suffix | `Reader`, `Writer`, `Stringer` |
| Acronyms | ALL CAPS | `HTTP`, `URL`, `ID` |

### Idioms

```go
// ✅ Constructor function
func NewUserService(repo UserRepository, logger *slog.Logger) *UserService {
    return &UserService{repo: repo, logger: logger}
}

// ✅ Error handling — Go-idiomatic
func (s *UserService) GetUser(ctx context.Context, id int64) (*User, error) {
    if id <= 0 {
        return nil, fmt.Errorf("invalid user ID: %d", id)
    }
    user, err := s.repo.FindByID(ctx, id)
    if err != nil {
        return nil, fmt.Errorf("finding user %d: %w", id, err)
    }
    return user, nil
}

// ✅ Sentinel errors
var (
    ErrUserNotFound   = errors.New("user not found")
    ErrDuplicateEmail = errors.New("email already exists")
)

// ✅ Small interfaces, defined at the usage site
type UserReader interface {
    FindByID(ctx context.Context, id int64) (*User, error)
}

// ✅ Table-driven tests
func TestCalculateDiscount(t *testing.T) {
    tests := []struct {
        name     string
        amount   float64
        tier     string
        expected float64
    }{
        {"no discount for basic", 100, "basic", 0},
        {"10% for premium", 100, "premium", 10},
        {"20% for vip", 100, "vip", 20},
    }
    for _, tt := range tests {
        t.Run(tt.name, func(t *testing.T) {
            got := CalculateDiscount(tt.amount, tt.tier)
            if got != tt.expected {
                t.Errorf("got %f, want %f", got, tt.expected)
            }
        })
    }
}
```

---

## 🔧 C++

### Formatting

```
INDENTATION=4 spaces
LINE_LENGTH=120
STANDARD=C++17 minimum, C++20 preferred
BRACES=same line (K&R) or Allman (project dependent)
HEADER_GUARD=#pragma once
```

### Naming Conventions

| Element | Style | Example |
|---------|-------|---------|
| Variables | camelCase | `playerHealth`, `movementSpeed` |
| Functions | PascalCase | `ProcessInput()`, `CalculateDamage()` |
| Classes/Structs | PascalCase | `PlayerController`, `NetworkPacket` |
| Constants | kPascalCase | `kMaxPlayers`, `kDefaultName` |
| Members | m_ prefix | `m_health`, `m_speed`, `m_name` |
| Namespaces | snake_case | `game_engine`, `network::protocol` |
| Templates | T prefix | `TValue`, `TAllocator` |
| Macros | UPPER_SNAKE | `UNLIKELY(x)` |
| Files | snake_case | `player_controller.h` / `.cpp` |

### Modern C++ Patterns

```cpp
// ✅ Smart pointers ALWAYS, never raw new/delete
auto player = std::make_unique<Player>("John", 100);
auto texture = std::make_shared<Texture>("hero.png");

// ✅ std::optional instead of magic values
std::optional<User> FindUser(int id) {
    auto it = m_users.find(id);
    if (it == m_users.end()) return std::nullopt;
    return it->second;
}

// ✅ std::string_view for read-only strings
void PrintName(std::string_view name) {
    std::cout << "Hello, " << name << "\n";
}

// ✅ Structured bindings (C++17)
auto [x, y, z] = GetPosition();
for (const auto& [key, value] : configMap) {
    ProcessConfig(key, value);
}

// ✅ constexpr for compile-time
constexpr int Factorial(int n) {
    if (n <= 1) return 1;
    return n * Factorial(n - 1);
}
static_assert(Factorial(5) == 120);

// ✅ Concepts (C++20)
template <typename T>
concept Numeric = std::integral<T> || std::floating_point<T>;

template <Numeric T>
T Clamp(T value, T min, T max) {
    return std::max(min, std::min(value, max));
}

// ✅ std::format (C++20)
auto message = std::format("Player {} has {} HP", player.name, player.health);

// ✅ Ranges (C++20)
auto activeNames = players
    | std::views::filter([](const Player& p) { return p.IsActive(); })
    | std::views::transform([](const Player& p) { return p.GetName(); })
    | std::views::take(10);
```

### Class Design

```cpp
// ✅ Rule of Zero — no custom destructor/copy/move if not needed
class UserProfile {
public:
    UserProfile(std::string name, std::string email)
        : m_name(std::move(name))
        , m_email(std::move(email))
    {}

    [[nodiscard]] const std::string& GetName() const noexcept { return m_name; }
    [[nodiscard]] const std::string& GetEmail() const noexcept { return m_email; }

private:
    std::string m_name;
    std::string m_email;
};

// ✅ Rule of Five — when managing a resource
class FileHandle {
public:
    explicit FileHandle(const std::filesystem::path& path);
    ~FileHandle();
    FileHandle(FileHandle&& other) noexcept;
    FileHandle& operator=(FileHandle&& other) noexcept;
    FileHandle(const FileHandle&) = delete;
    FileHandle& operator=(const FileHandle&) = delete;
private:
    FILE* m_handle = nullptr;
};

// ✅ Interfaces via pure virtual classes
class IRenderer {
public:
    virtual ~IRenderer() = default;
    virtual void DrawSprite(const Sprite& sprite, Vec2 position) = 0;
    virtual void Present() = 0;
    IRenderer(const IRenderer&) = delete;
    IRenderer& operator=(const IRenderer&) = delete;
protected:
    IRenderer() = default;
};
```

### Error Handling

```cpp
// ✅ Custom exception hierarchy
class NetworkError : public std::runtime_error {
public:
    NetworkError(std::string_view message, int errorCode)
        : std::runtime_error(std::string(message)), m_errorCode(errorCode) {}
    [[nodiscard]] int GetErrorCode() const noexcept { return m_errorCode; }
private:
    int m_errorCode;
};

// ✅ std::expected (C++23)
[[nodiscard]] std::expected<User, std::string> ParseUser(std::string_view json);

// ✅ [[nodiscard]] for functions where ignoring result is a bug
[[nodiscard]] bool Initialize();
[[nodiscard]] std::error_code SaveFile(const std::filesystem::path& path);
```

### Headers

```cpp
// ✅ #pragma once
#pragma once

#include <memory>
#include <string>

// ✅ Forward declarations instead of #include where possible
class InputManager;
class PhysicsWorld;

namespace game {
class PlayerController final { ... };
} // namespace game
```

---

## 💜 C#

### Formatting

```
INDENTATION=4 spaces
BRACES=next line (Allman)
NAMESPACE=file-scoped (C# 10+)
NULLABLE=enabled (#nullable enable)
```

### Naming Conventions

| Element | Style | Example |
|---------|-------|---------|
| Variables | camelCase | `userName`, `orderCount` |
| Methods | PascalCase | `GetUser()`, `ProcessPayment()` |
| Classes | PascalCase | `PaymentService`, `UserRepository` |
| Interfaces | I + PascalCase | `IPlayerService`, `IRepository<T>` |
| Properties | PascalCase | `Name`, `IsActive`, `Health` |
| Private fields | _camelCase | `_logger`, `_currentHealth` |
| Constants | PascalCase | `MaxPlayers`, `DefaultName` |
| Events | PascalCase | `DamageReceived`, `OrderCompleted` |
| Generics | T prefix | `TEntity`, `TResult` |
| Async methods | Async suffix | `GetUserAsync()`, `SaveChangesAsync()` |
| Files | PascalCase | `PlayerController.cs`, `IUserService.cs` |

### Modern C# Patterns

```csharp
// ✅ Records for immutable DTOs
public record UserProfile(string Name, string Email, DateTimeOffset CreatedAt);

// ✅ Primary constructors (C# 12)
public class OrderService(
    IOrderRepository repository,
    ILogger<OrderService> logger)
{
    public async Task<Order> CreateOrderAsync(CreateOrderRequest request)
    {
        logger.LogInformation("Creating order for {UserId}", request.UserId);
        var order = Order.Create(request);
        await repository.AddAsync(order);
        return order;
    }
}

// ✅ Required members (C# 11)
public class CreateUserRequest
{
    public required string Name { get; init; }
    public required string Email { get; init; }
    public string? Phone { get; init; }
}

// ✅ Pattern matching — exhaustive
public decimal CalculateDiscount(Customer customer) => customer switch
{
    { Tier: CustomerTier.Vip, YearsActive: > 5 } => 0.25m,
    { Tier: CustomerTier.Vip } => 0.15m,
    { Tier: CustomerTier.Premium } => 0.10m,
    _ => 0m,
};

// ✅ Raw string literals (C# 11)
var json = """
    {
        "name": "John",
        "email": "john@example.com"
    }
    """;

// ✅ Collection expressions (C# 12)
int[] numbers = [1, 2, 3, 4, 5];
```

### Async/Await

```csharp
// ✅ CancellationToken ALWAYS in signatures
public async Task<UserProfile> GetProfileAsync(
    int userId,
    CancellationToken cancellationToken = default)
{
    var response = await _httpClient.GetAsync(
        $"/api/users/{userId}", cancellationToken);
    response.EnsureSuccessStatusCode();
    return await response.Content
        .ReadFromJsonAsync<UserProfile>(cancellationToken: cancellationToken)
        ?? throw new InvalidOperationException("Failed to deserialize");
}

// ✅ Parallel tasks
var profileTask = GetProfileAsync(userId, ct);
var ordersTask = GetOrdersAsync(userId, ct);
await Task.WhenAll(profileTask, ordersTask);

// ❌ NEVER .Result or .Wait() — deadlock risk
// ❌ NEVER async void — only for event handlers
```

### Dependency Injection

```csharp
// ✅ Constructor injection ALWAYS
public class UserService : IUserService
{
    private readonly IUserRepository _repository;
    private readonly ILogger<UserService> _logger;

    public UserService(IUserRepository repository, ILogger<UserService> logger)
    {
        _repository = repository ?? throw new ArgumentNullException(nameof(repository));
        _logger = logger ?? throw new ArgumentNullException(nameof(logger));
    }
}

// ✅ Registration extensions
public static class ServiceCollectionExtensions
{
    public static IServiceCollection AddApplicationServices(this IServiceCollection services)
    {
        services.AddScoped<IUserService, UserService>();
        services.AddSingleton<ICacheService, RedisCacheService>();
        return services;
    }
}
```

### LINQ

```csharp
// ✅ Method syntax for most cases
var activeAdmins = users
    .Where(u => u.IsActive && u.Role == UserRole.Admin)
    .OrderByDescending(u => u.LastLoginAt)
    .Select(u => new UserSummary(u.Id, u.Name))
    .ToList();

// ✅ Query syntax for complex joins/groups
var report =
    from order in orders
    join customer in customers on order.CustomerId equals customer.Id
    group order by customer.Name into g
    select new { Customer = g.Key, Total = g.Sum(o => o.Amount) };
```

### Error Handling

```csharp
// ✅ Custom domain exceptions
public class UserNotFoundException : DomainException
{
    public int UserId { get; }
    public UserNotFoundException(int userId)
        : base("USER_NOT_FOUND", $"User {userId} not found") => UserId = userId;
}

// ✅ Result pattern alternative
public class Result<T>
{
    public T? Value { get; }
    public string? Error { get; }
    public bool IsSuccess => Error is null;
    public static Result<T> Success(T value) => new() { Value = value };
    public static Result<T> Failure(string error) => new() { Error = error };
}
```

---

## 🎨 HTML / CSS

### HTML Structure

```html
<!-- ✅ Semantic HTML5 -->
<header class="site-header">
  <nav class="main-nav" aria-label="Main navigation">
    <a href="/" class="nav-logo">Brand</a>
    <ul class="nav-links">
      <li><a href="/about">About</a></li>
    </ul>
  </nav>
</header>
<main class="content">
  <article class="post">...</article>
</main>
<footer class="site-footer">...</footer>

<!-- Attributes order: id, class, data-*, other -->
<div id="main" class="container" data-page="home" role="main">
```

### CSS Conventions

```css
/* ✅ Custom Properties (Design Tokens) */
:root {
  --color-primary: #6366f1;
  --color-primary-hover: #4f46e5;
  --color-text: #1f2937;
  --color-text-muted: #6b7280;
  --color-bg: #ffffff;

  --font-sans: 'Inter', system-ui, sans-serif;
  --font-mono: 'JetBrains Mono', monospace;

  --radius-sm: 0.375rem;
  --radius-md: 0.5rem;
  --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.05);

  --transition-fast: 150ms ease;
  --transition-normal: 200ms ease;
}

/* ✅ BEM-like naming */
.component { }
.component__element { }
.component--modifier { }

/* ✅ Property order: positioning → box model → typography → visual */
.element {
  position: relative;
  top: 0;

  display: flex;
  width: 100%;
  padding: 1rem;

  font-size: 1rem;
  color: var(--color-text);

  background: var(--color-bg);
  border-radius: var(--radius-md);
  transition: box-shadow var(--transition-normal);
}

/* ✅ Responsive: mobile-first */
.grid {
  display: grid;
  gap: 1.5rem;
  grid-template-columns: 1fr;
}

@media (min-width: 768px) {
  .grid { grid-template-columns: repeat(2, 1fr); }
}

@media (min-width: 1024px) {
  .grid { grid-template-columns: repeat(3, 1fr); }
}
```

---

## 🐍 Django Templates

### Tag Formatting

```django
{# CRITICAL: Tags must be on ONE LINE #}

✅ Correct:
{% if user == job.employer and not app.employer_signature or user == artist.user and not app.artist_signature %}

❌ Wrong (will cause TemplateSyntaxError):
{% if user == job.employer and not app.employer_signature or user == artist.user and not
app.artist_signature %}
```

### Comparison Operators

```django
{# CRITICAL: Spaces around == #}

✅ Correct:
{% if request.GET.gender == 'M' %}

❌ Wrong:
{% if request.GET.gender=='M' %}
{% if request.GET.gender =='M' %}
```

---

## 🗄️ SQL

### Formatting

```
KEYWORDS=UPPERCASE (SELECT, FROM, WHERE, JOIN)
IDENTIFIERS=snake_case
TABLES=singular (user, order, payment)
INDENT=2 or 4 spaces for sub-clauses
```

### Idioms

```sql
-- ✅ CTE instead of nested subqueries
WITH active_users AS (
    SELECT id, name, email, created_at
    FROM "user"
    WHERE is_active = TRUE
      AND last_login_at > CURRENT_DATE - INTERVAL '30 days'
),
user_orders AS (
    SELECT user_id, COUNT(*) AS order_count,
           SUM(total_amount) AS total_spent
    FROM "order"
    WHERE status = 'completed'
    GROUP BY user_id
)
SELECT
    au.name,
    au.email,
    COALESCE(uo.order_count, 0) AS order_count,
    COALESCE(uo.total_spent, 0.00) AS total_spent
FROM active_users au
LEFT JOIN user_orders uo ON uo.user_id = au.id
ORDER BY uo.total_spent DESC NULLS LAST
LIMIT 100;

-- ✅ Safe migrations
ALTER TABLE "user"
    ADD COLUMN IF NOT EXISTS verified_at TIMESTAMPTZ DEFAULT NULL;

-- ✅ Concurrent indexes for production
CREATE INDEX CONCURRENTLY IF NOT EXISTS
    idx_user_email ON "user" (email);
```

---

## 🔀 Language Comparison Quick Reference

| Aspect | Python | TypeScript | Java | C++ | C# | Rust | Go |
|--------|--------|-----------|------|-----|-----|------|-----|
| **Variables** | snake_case | camelCase | camelCase | camelCase | camelCase | snake_case | camelCase |
| **Functions** | snake_case | camelCase | camelCase | PascalCase | PascalCase | snake_case | PascalCase |
| **Classes** | PascalCase | PascalCase | PascalCase | PascalCase | PascalCase | PascalCase | PascalCase |
| **Constants** | UPPER_SNAKE | UPPER_SNAKE | UPPER_SNAKE | kPascalCase | PascalCase | UPPER_SNAKE | PascalCase |
| **Private** | _prefix | private | private | m_ prefix | _prefix | pub(crate) | lowercase |
| **Files** | snake_case | kebab-case | PascalCase | snake_case | PascalCase | snake_case | snake_case |
| **Indent** | 4 spaces | 2 spaces | 4 spaces | 4 spaces | 4 spaces | 4 spaces | tabs |
| **Null-safe** | Optional | T \| null | Optional<T> | std::optional | T? | Option<T> | nil check |
| **Error** | try/except | try/catch | try/catch | exceptions | try/catch | Result<T,E> | error |
