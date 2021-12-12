package main

import scala.concurrent.duration._
import io.gatling.core.Predef._
import io.gatling.http.Predef._

object Random {
  def randomString(length: Int): String = {
    val SALTCHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    val salt = new StringBuilder
    val rnd = new scala.util.Random
    while (salt.length < length) { // length of the random string.
      val index = (rnd.nextFloat() * SALTCHARS.length).asInstanceOf[Int]
      salt.append(SALTCHARS.charAt(index))
    }
    val saltStr = salt.toString
    saltStr
  }

  def randomInt(count: Int): Int ={
    new scala.util.Random().nextInt(count)
  }

  def randomPostRequest() : String =  """{"id":"""".stripMargin + randomInt(999) + """",
                                        "title":"""".stripMargin + Random.randomString(15) + """",
                                        "body":"""".stripMargin + Random.randomString(15) + """",
                                        "userId":""".stripMargin + randomInt(999) + "}" 
}

class UserSimulation extends Simulation {
  val httpProtocol = http
    .baseUrl("https://jsonplaceholder.typicode.com")

  val post = scenario("Post new Post")
    .exec(sessionPost => {
      val sessionPostUpdate = sessionPost.set("postrequest", Random.randomPostRequest())
      sessionPostUpdate
    })
    .exec(
      http("Post new Post")
        .post("/posts")
          .body(StringBody("${postrequest}")).asJson
    )

  val get = scenario("Get Post")
    .exec(sessionPost => {
      val sessionPostUpdate = sessionPost.set("postrequest", Random.randomPostRequest())
      sessionPostUpdate
    })
    .exec(
      http("Post new Post")
        .post("/posts")
        .body(StringBody("${postrequest}")).asJson
        .check(jsonPath("$.id").saveAs("id"))
    )
    .exitHereIfFailed
    .exec(
      http("Get Post")
        .get("/posts/19")
    )

  val put = scenario("Put Post")
    .exec(sessionPost => {
      val sessionPostUpdate = sessionPost.set("postrequest", Random.randomPostRequest())
      sessionPostUpdate
    })
    .exec(
      http("Post new Post")
        .post("/posts")
        .body(StringBody("${postrequest}")).asJson
        .check(jsonPath("$.id").saveAs("id"))
    )
    .exitHereIfFailed
    .exec(sessionPut => {
      val sessionPutUpdate = sessionPut.set("putrequest", Random.randomPostRequest())
      sessionPutUpdate
    })
    .exec(
      http("Put Post")
        .put("/posts/10")
        .body(StringBody("${putrequest}")).asJson
    )

  val delete = scenario("Delete Post")
    .exec(sessionPost => {
      val sessionPostUpdate = sessionPost.set("postrequest", Random.randomPostRequest())
      sessionPostUpdate
    })
    .exec(
      http("Post new Post")
        .post("/posts")
        .body(StringBody("${postrequest}")).asJson
        .check(jsonPath("$.id").saveAs("id"))
    )
    .exitHereIfFailed
    .exec(sessionPut => {
      val sessionPutUpdate = sessionPut.set("putrequest", Random.randomPostRequest())
      sessionPutUpdate
    })
    .exec(
      http("Delete Post")
        .delete("/posts/${id}")
    )

  setUp(post.inject(rampUsers(15).during(30.seconds)).protocols(httpProtocol),
    get.inject(rampUsers(15).during(30.seconds)).protocols(httpProtocol),
    put.inject(rampUsers(15).during(30.seconds)).protocols(httpProtocol),
    delete.inject(rampUsers(15).during(30.seconds)).protocols(httpProtocol))
}