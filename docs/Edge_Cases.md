# Edge Cases – API Automation

## 1️⃣ Purchase API
- Invalid card number (all zeros, or unsupported BIN)
- Expired card
- Missing mandatory field `account_id`
- Amount exceeds limit
- Invalid currency code
- Duplicate idempotency key

## 2️⃣ Refund API
- Refund amount greater than original payment
- Refund with invalid payment ID
- Refund without authorization
- Missing mandatory field `reason`
- Duplicate refund request (idempotency)

## 3️⃣ Authorization API
- Zero or negative amount
- Invalid card number
- Missing `workflow` field
- Expired card
- Unsupported currency

## 4️⃣ Capture API
- Capture before authorization
- Capture with invalid payment ID
- Capture already captured payment
- Partial capture exceeding amount

## 5️⃣ Cancel API
- Cancel after capture
- Cancel with invalid payment ID
- Cancel non-existent payment
- Cancel multiple times on same payment

## 6️⃣ Verify API
- Verify with invalid payment ID
- Verify before purchase created
- Verify with unauthorized API key
- Verify after cancellation

## 7️⃣ Customer API
- Invalid email format
- Missing mandatory fields (`name`)
- Duplicate customer creation
- Unsupported characters in name/email

## 8️⃣ Enrollment API
- Invalid customer ID
- Expired card
- Missing mandatory fields (`card_number`, `expiry_month`, `cvv`)
- Duplicate enrollment for same card
- Unsupported card type
