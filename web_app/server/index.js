import app from "./app";
import db from './db';

app.listen(7000, function() {
  console.info(`Server started listening on port 7000.`);
});
process.on('uncaughtException', function (err) {
  console.log(err);
}); 
process.on('SIGINT', function() {
  console.log(`Gracefully shutting down from SIGINT (Ctrl-C)`);
  db.connection.close();
  process.exit(1);
});
