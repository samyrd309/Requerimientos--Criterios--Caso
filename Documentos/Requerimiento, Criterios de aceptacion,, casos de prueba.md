

# Requirements 
## Functional 
* It must be possible to insert values ​​in a range greater than 0 and less than 2000000. 
* The system must accept only numeric values ​​per screen. 
* The system must not accept empty values.
* The system must present the decimal values ​​entered per screen, in Roman numerals. 
## Non-Functional 
* Roman numerals I, X, C, and M must be repeated three times when writing a composite number. 
* The numbers V, L, and D cannot be repeated. 
* Values ​​of compound Roman numerals must be added whenever the value on the right is less than the value on the left. 
* The values ​​of compound Roman numerals that have a number on the right greater than the one on the left and this is I, X, or C, then the one on the left must be subtracted from the right. 
* Roman numerals that have a quote(`), its value is multiplied by a thousand. 
# User Story 
* User story 1: As a user, I want to be able to insert values ​​from 0 to 1999999, convert them to Roman numerals, and display them on the screen.
 # Criteria of acceptance 

## 
**User story 1**
 * As a user, I want to be able to insert values ​​from 0 to 1999999, convert them to Roman numerals, and display them on the screen. 
---- 
---- 
### **CA.1 Invalid values**
#### **Scenario 1: You enter a null value.**
 * *Given*: "Insert a number" appears on the screen. 
* *Then*: The user inserts the number. 
* *When*: The user presses enter.
 * *Then*: The system displays "WARNING: invalid number entered"
 --- 
#### **Scenario 2: Enter a text type value.** 
* *Given*: "Insert a number" appears on the screen.
 * *Then*: The user inserts a text type value. 
* *When*: The user presses enter. 
* *Then*: system displays "WARNING: invalid number entered" 
---- 
### **CA.2 Values out of the range**
#### **Scenario 1: A value less than 0 is entered.** 
* *Given* : "Insert a number" is displayed.
 * *Then*  : The user inserts a value less than 0. 
* *When*: The user presses enter.
 * *Then*: The system displays "WARNING: Please enter a number less than 20000000 and greater than 0."
 ---- 

  #### **Scenario 2: A value greater than 1999999 is entered.**
 * *Given*: "Insert a number" appears on the screen.
 * *Then*: The user inserts a value greater than 1999999. 
* *And*: The user presses enter. * *Then*: The system displays "WARNING: Please enter a number less than 20000000 and greater than 0." 
---- 
### **CA.2 Values in the range**
#### **Scenario 1: A value less than 20000000 and greater than 0 is entered.** 
* *Given*: "Insert a number" appears on the screen.
 * *When*: The user enters a value less than 20000000 and greater than 0. 
* *And*: The user presses enter. 
* *Then*: The system displays the number inserted by the user on the screen. ---- # Test cases ## End-to-End (From UI) ##

# Test Case
## End-to-End (from the UI)

* CP-0: Insert null values
* CP-1: Insert text values
* CP-2: Insert integer values
* CP-3: Insert values ​​less than 0
* CP-4: Insert values ​​greater than 1999999
* CP-5: Insert values ​​greater than 0 and less than 1999999

## Unitarios 


 