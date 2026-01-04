# Requirements – API Automation Assessment

## 1️⃣ Functional Requirements
- Create, refund, authorize, capture, cancel, verify payments  
- Create and manage customer records  
- Enroll cards for customers  
- Mandatory field `workflow = DIRECT` for all payments  
- Support minimal and maximal payloads  
- Support idempotency for payment requests  
- Handle headers: public-api-key, private-secret-key, x-idempotency-key  
- API responses must be validated (status codes + optional response body checks)  
- Support negative scenarios and edge cases

## 2️⃣ Non-Functional Requirements
- All tests must run via **Behave BDD framework**  
- API client should be **reusable and scalable**  
- Step files should handle **dynamic payloads and headers**  
- Default payloads and headers centralized in **config.py**  
- Logging or print statements should allow **debugging responses**  
- Test framework should support **future API additions** without major changes  
- Execution should be simple: `python -m behave`  
- Tags for scenarios: @sanity, @regression, @integration

## 3️⃣ Documentation Requirements
- Test cases clearly documented in `Test_Cases.md`  
- Edge and negative scenarios documented in `Edge_Cases.md`  
- Requirements captured in `Requirements.md`  

## 4️⃣ Optional / Bonus
- Critical thinking scenarios, e.g., multiple captures, refunds exceeding payments  
- Dynamic headers and payloads for runtime overrides  
- Modular architecture similar to **Page Object Model** for APIs
