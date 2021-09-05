# 섹션 3: Your first REST API
> https://www.udemy.com/course/rest-api-flask-and-python/learn/lecture/5960110#overview

---


# 53. What is an API?
1분

# 54. Installing Flask
2분

# 55. Access the code for this section here
1분

# 56. Your first Flask application


# 57. HTTP Verbs




> The server then sees GET /  HTTP/1.1

1. GET : Verb
2. / : Path
3. HTTP/1.1 : Protocol

---

> https://twitter.com/login
---

`GET /login HTTP/1.1 `\
`Host: https://twitter.com` 


---

> https://git-scm.com/download/mac
---

`GET /download/mac HTTP/1.1 `\
`Host: https://git-scm.com/`

### summary

1.  페이지를 갈때는 항상 get을 쓴다.
2. 하지만 아래와같이 많은 메소드 들이 있다. POST, DELETE, PUT, OPTIONS, HEAD, ....
3. 각각 서버는 개개인에게 다른 응답을 주지만 보통은 비슷하게 준다.

---

| VERB   | MEANING                     | EXAMPLE        |   |   |
|--------|-----------------------------|----------------|---|---|
| GET    | Retrieve something          | GET /item/1    |   |   |
| POST   | Receive data, and use it    | POST /item     |   |   |
| PUT    | Make sure soething is there | PUT /item      |   |   |
| DELETE | Remove something            | DELETE /item/1 |   |   |




58. REST Principles

복습

1. Site 갈때는 get 요청
2. 1.하는 경우 보통 html 준다

## REST API란?

> It is a way of thinking about how a web server responds to you  requests.
> It doesn't respond with just data
> It responds with Resources.


## Resources 란?
> Similar to object-oriented programming
> Think of ther Server as having resources, and each is able to interact with the pertinent request

* pertinent(relevant, 적절한, 관련있는)
  
## Stateless란?

> Another Key feature is that REST is supposed to be stateless
> this means one request cannot depend on any other requests
> The server only knows about the current request, and not any previous requests.
 
### Example

`POST /item/chair` creates an item

서버는 item이 존재하는지 모른다.

`GET /item/chair` 는 DB에가서 아이템이 있는지 체크한다.

to get an item you don't need to have created an item before,
the item could be in the db from previously.





59. Creating our application endpoints




60. Returning a list of stores
7분

61. Implementing other endpoints
9분

62. Calling the API from JavaScript
7분

63. Using Postman for API testing
```

