var db = require("mongoose");

const ATLAS_SECRET = "-----secret-----",
  ATLAS_USER = "ezid_usr",
  CONECTION_URL =
    "mongodb+srv://" +
    ATLAS_USER +
    ":" +
    ATLAS_SECRET +
    "@ezid-8j9dg.gcp.mongodb.net/test?retryWrites=true&w=majority";

db.connect(CONECTION_URL, { dbName: "ezid", useNewUrlParser: true });
db.set("debug", true);
db.connection.on("error", function(err) {
  console.error("connection error", err);
});
db.connection.once("open", function() {
  console.log("Mongo DB: we're connected!");
});
export default db;
