# Test Cases – API Automation

## 1️⃣ Purchase API
| Scenario | Type | Payload | Expected Status |
|----------|------|--------|----------------|
| Minimal fields | Positive | DEFAULT_PAYLOAD | 201 |
| Maximal fields | Positive | customer_payer + additional_data | 201 |
| Invalid card | Negative | Invalid card number | 400 |
| Missing account_id | Negative | account_id=None | 400 |

## 2️⃣ Refund API
| Scenario | Type | Payload | Expected Status |
|----------|------|--------|----------------|
| Minimal fields | Positive | DEFAULT_REFUND_PAYLOAD | 201 |
| Maximal fields | Positive | reason + note | 201 |
| Excessive amount | Negative | amount > payment | 400 |
| Invalid payment_id | Negative | payment_id="invalid_id" | 400 |

## 3️⃣ Authorization API
| Scenario | Type | Payload | Expected Status |
|----------|------|--------|----------------|
| Minimal fields | Positive | DEFAULT_AUTHORIZATION_PAYLOAD | 201 |
| Maximal fields | Positive | customer_payer + additional_data | 201 |
| Amount zero | Negative | amount=0 | 400 |
| Invalid card | Negative | card_number invalid | 400 |

## 4️⃣ Capture API
| Scenario | Type | Payload | Expected Status |
|----------|------|--------|----------------|
| Capture authorized | Positive | payment_id valid | 201 |
| Invalid payment_id | Negative | payment_id invalid | 400 |
| Capture without auth | Negative | payment_id=None | 400 |

## 5️⃣ Cancel API
| Scenario | Type | Payload | Expected Status |
|----------|------|--------|----------------|
| Cancel authorized | Positive | payment_id valid | 201 |
| Invalid payment_id | Negative | payment_id invalid | 400 |
| Cancel captured | Negative | payment_id captured | 400 |

## 6️⃣ Verify API
| Scenario | Type | Payload | Expected Status |
|----------|------|--------|----------------|
| Verify valid payment | Positive | payment_id valid | 200 |
| Invalid payment_id | Negative | payment_id invalid | 400 |
| Payment not created | Negative | payment_id nonexistent | 404 |

## 7️⃣ Customer API
| Scenario | Type | Payload | Expected Status |
|----------|------|--------|----------------|
| Minimal fields | Positive | DEFAULT payload | 201 |
| Maximal fields | Positive | name + email + phone | 201 |
| Invalid email | Negative | email invalid | 400 |
| Missing name | Negative | name None | 400 |

## 8️⃣ Enrollment API
| Scenario | Type | Payload | Expected Status |
|----------|------|--------|----------------|
| Minimal fields | Positive | DEFAULT payload | 201 |
| Maximal fields | Positive | card + customer_id | 201 |
| Invalid customer_id | Negative | customer_id invalid | 400 |
| Expired card | Negative | expiry_year past | 400 |
