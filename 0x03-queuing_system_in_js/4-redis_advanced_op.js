import { createClient } from "redis";

const client = createClient()
  .on("error", (err) => {
    console.log("Redis client not connected to the server: " + err);
  })
  .on("connect", () => {
    console.log("Redis client connected to the server");
  });

client.hset(
  "HolbertonSchools",
  "Portland",
  50,
  "Seattle",
  80,
  "New York",
  20,
  "Bogota",
  20,
  "Cali",
  40,
  "Paris",
  2,
  (err, reply) => {
    if (err) console.error(err);
    console.log(`Reply: ${reply}`);
  },
);

client.hgetall("HolbertonSchools", (err, object) => {
  if (err) console.error(err);
  console.log(object);
});
