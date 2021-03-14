# sales_cards
##  requests

* /get_users_cards
  type:
    get
  params:
  - user_id
  describtion:
  get user's aviable cards by user's id

* /register
  type:
    post
  params:
  - phone_number: string
  - name : string
  describtion:
  register new user

* /get_all_users
  type:
    get
  params:
    no params provided
  describtion:
  return all users with related sales cards
  
* /remove_ures
  type:
    post
  params:
    user_id
  describtion:
  remove user from db with related cards
