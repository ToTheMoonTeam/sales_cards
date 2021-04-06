# sales_cards - requests

## /get_users_cards
**type:** get
  
**params:**
  - user_id

**describtion:** get user's aviable cards by user's id and users's data
  
can get message: empty database if db is empty

## /register
  
**type:** post
  
**params:**
  - phone_number: string
  - name : string
  - birthday : datetime
  - work_quality : integer
  - shipping_quality : integer
  
**describtion:** register new user
  
return users's data after registration
  
## /get_all_users
  
**type:** get
  
**params:**
  - no params provided

**describtion:** return all users with related sales cards
    
can get message: empty database if db is empty
flask_cors

## /remove_user
  
**type:** post
  
**params:**
  - user_id
  
**describtion:** remove user from db with related cards
  
can get message: empty database if db is empty

## /register_card

**type:** post
  
**params:**
  - company_name: string
  - sale: double
  - id(optional): int manualy added id or auto-incremented

**describtion:** return all cards
    
can get message: empty database if db is empty
  
## /get_all_cards

**type:** get
  
**params:**
  - no params provided

**describtion:** return all cards 
    
can get message: empty database if db is empty

## /link_card
  
**type:** post
    
**params:**
  - user_id: int
  - card_id: int
  
**describtion:** link sales card to user

return card and user that was linked
  
