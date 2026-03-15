# Python-ATM-Machine

A command-line ATM system I built to practice Python. It uses `json` to actually save and remember user accounts, balances, and PINs between sessions
**What this project does:**
1. **Persistent Data Storage:** Uses `json` to read and write user balances and PINs to an `atm_details.json` file.
2. **Account Creation:** New users can register, set a PIN, and get an auto-generated User ID.
3.  **Standard ATM Functions:** Users can deposit, withdraw, and check their balance (requires correct PIN validation).
4.  **Bank Vault Constraints:** The bank itself has a total vault limit. If the bank runs out of money, large withdrawals are blocked.
5.  **Secret Admin Menu:** Built a hidden admin login to track total bank funds and user lists.

**How to test the Admin Menu:**
If you want to see the admin side of the system, run the code and use these credentials:
* **User ID:** `0000`
* **Password:** `rishit`
