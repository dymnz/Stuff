### Database - MongoDB
---
#### Customer
* name
* phone
* email
* purchases[]
    - date: STRING (YYYY_MM_DD)
    - stuff: STRING
    - amount: INT
    - price each: INT

---

#### Daily
* date: STRING (YYYY_MM_DD)
* customers[]
    - name
* purchases
    - Look for qualified "date" & "stuff" of each "name" in Customer

##### 1. Add stuff
1. Give a list of "customer-name" from **Customer**
2. Give a list of "stuff-name" from **Storage**
3. Look up "price each"/"amount" from **Storage**
4. Get amount of purchase and price each, calculate total
5. Add 
    1. In **Customer**, add "purchase" to "purchases[]" of "customer-name" ('$push')
    2. In **Daily**, add "customer-name" to "customers[]" of "date" (Check duplication, '$addToSet')
6. Update
    1. In **Storage**, update "amount" of "stuff-name"

##### 2. Remove stuff
1. Update
    1. In **Customer**, search for the purchase, pull "purchase" in "purchases[]"
    2. In **Daily**, check other purchases of "customer-name", if no other purchase of "date", update "customers[]"
    3. In **Storage**, update "amount" of "stuff-name"

---

#### Storage
* stuffs[]   (Current state)
    - name
    - amount
    - price each
* history[] (Import history)
    - name
    - amount
    - cost

##### 1. Add stuff
1. Add
    1. In **Storage**, add import info in "history[]"
2. Update
    1. In **Storage**, update "amount" of "stuff-name"
    
##### 2. New stuff
1. Add
    1. In **Storage**, add new stuff with "name" and "price" w/ "amount: 0"
