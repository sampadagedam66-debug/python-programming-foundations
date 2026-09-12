"""
variables_and_types.py

Topic: Variables and Data Types in Python
Covers: core types | type() vs isinstance() | mutability & id() |
        constants & naming convention | implicit vs explicit conversion |
        augmented assignment | float precision | bool-int duality
Mini use-case: an AI chatbot API usage billing calculator
"""

# ---------------------------------------------------------
# SECTION 1: Core data types — AI Chatbot Identity & Configuration
# ---------------------------------------------------------
print("---- Core Data Types: AI Chatbot Config ----")

bot_name = "NovaBot"
response_temperature = 0.7          # sampling temperature (0.0 - 1.0)
is_bot_online = True
total_messages_handled = 2450
last_error_code = None              # no errors logged yet

print(f"Bot Name: {bot_name}, type: {type(bot_name).__name__}, is_int: {isinstance(bot_name, int)}")
print(f"Response Temperature: {response_temperature}, type: {type(response_temperature).__name__}, is_int: {isinstance(response_temperature, int)}")
print(f"Is Online: {is_bot_online}, type: {type(is_bot_online).__name__}, is_int: {isinstance(is_bot_online, int)}")
print(f"Messages Handled: {total_messages_handled}, type: {type(total_messages_handled).__name__}, is_int: {isinstance(total_messages_handled, int)}")
print(f"Last Error Code: {last_error_code}, type: {type(last_error_code).__name__}, is_int: {isinstance(last_error_code, int)}")

# Note: isinstance(True, int) is True — bools are a subclass of int in Python.
# This matters later in the mini project below.


# ---------------------------------------------------------
# SECTION 2: Constants, mutability & conversion — Bot Runtime Settings
# ---------------------------------------------------------
print("\n---- Constants & Conversion: Bot Runtime Settings ----")

# ALL_CAPS is the naming convention for values that shouldn't be reassigned
MAX_TOKENS = 4096
MODEL_VERSION = "NovaBot-v2"
print(f"Model: {MODEL_VERSION}, Max Tokens per Response: {MAX_TOKENS}")

# int is immutable: reassigning creates a new object, id() changes
active_sessions = 12
print(f"\nactive_sessions = {active_sessions}, id = {id(active_sessions)}")
active_sessions = active_sessions + 1  # a new user just connected
print(f"active_sessions = {active_sessions}, id = {id(active_sessions)}  <- different id, new object")

# implicit conversion: Python upgrades int to float automatically here
total_storage_used_mb = 5000     # int
total_users = 30                  # int
average_storage_per_user_mb = total_storage_used_mb / total_users  # becomes float automatically
print(f"\nImplicit conversion: {total_storage_used_mb} / {total_users} = {average_storage_per_user_mb:.2f} "
      f"(type: {type(average_storage_per_user_mb).__name__})")

# explicit conversion: we choose the type ourselves
rounded_storage_per_user = int(average_storage_per_user_mb)  # explicitly truncates to int
print(f"Explicit conversion: int({average_storage_per_user_mb:.2f}) = {rounded_storage_per_user}")


# ---------------------------------------------------------
# SECTION 3: Augmented assignment & float precision — Conversation Counters
# ---------------------------------------------------------
print("\n---- Augmented Assignment & Float Precision: Conversation Stats ----")

messages_handled_today = 0
messages_handled_today += 180   # morning shift traffic
messages_handled_today += 95    # evening shift traffic
print(f"Total messages handled today: {messages_handled_today}")

# classic float precision quirk — shows up when adding small file sizes
log_chunk_1_mb = 0.1
log_chunk_2_mb = 0.2
total_log_size_mb = log_chunk_1_mb + log_chunk_2_mb
print(f"Total log file size: {log_chunk_1_mb} + {log_chunk_2_mb} = {total_log_size_mb} "
      f"(not exactly 0.3, due to float precision)")
print(f"Rounded properly: {round(total_log_size_mb, 2)}")


# ---------------------------------------------------------
# SECTION 4: Mini Project — AI Chatbot API Usage Billing Calculator
# ---------------------------------------------------------
# Real use of everything above: type casting on input, and the
# bool-int trick replaces an if/else for the pro discount
# (control flow is a separate topic file).

print("\n---- Mini Project: AI Chatbot API Billing ----")

BASE_SUBSCRIPTION_PRICE = 499
INCLUDED_TOKENS = 100000
PRICE_PER_EXTRA_1K_TOKENS = 0.8
PRO_MEMBER_DISCOUNT_RATE = 0.20

tokens_used_this_month = float(input("Enter tokens used this month: "))
extra_tokens = max(0, tokens_used_this_month - INCLUDED_TOKENS)
extra_cost = (extra_tokens / 1000) * PRICE_PER_EXTRA_1K_TOKENS

is_pro_member = input("Are you a Pro subscriber? (y/n): ").strip().lower() == "y"
# bool * float works because True == 1 and False == 0 in Python
discount_amount = extra_cost * PRO_MEMBER_DISCOUNT_RATE * is_pro_member

final_cost = BASE_SUBSCRIPTION_PRICE + extra_cost - discount_amount

print("\n----- AI API USAGE BILL -----")
print(f"Base Subscription ({INCLUDED_TOKENS} tokens included): Rs {BASE_SUBSCRIPTION_PRICE}")
print(f"Extra Tokens Used: {extra_tokens:.0f}")
print(f"Extra Usage Cost: Rs {extra_cost:.2f}")
print(f"Pro Member Discount: Rs {discount_amount:.2f}")
print(f"TOTAL: Rs {final_cost:.2f}")
