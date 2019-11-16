import express from "express";
import compression from "compression";
import bodyparser from "body-parser";
import routes from "./routes";


console.info("Initializing express.");
const app = express();
console.info("Express intialized.");


//=============================MIDDLEWARE STARTS======================//
/*USING COMPRESSION MIDDLEWARE*/
// for defalate || gzip compression encodings on response bodies
app.use(compression(/*options*/));
console.info("Compression middleware registered.");
//options[object] => with keys
//'chunkSize',
//'filter' - [when & when not to compress],
//'level' - [range from (-1) to (+9), 9 means highly compressed]
/*----------------------------*/

/*USING BODY PARSER MIDDLEWARE*/
//parses the JSON, buffer, string and URL encoded data submitted using HTTP POST & exposes it on req.body
app.use(bodyparser.json()); // support json encoded bodies
console.info("Bodyparser middleware registered.");
/*----------------------------*/

//=============================MIDDLEWARE ENDS========================//

/*ROUTES*/
console.info("Registering routes.....");
routes(app);
console.info("Route registration complete..");
/*ROUTES*/

/*USING EXPRESS STATIC MIDDLEWARE*/
//serve files from within a given root directory
// app.use(express.static(path.join(__dirname, "../")));
// console.info("Express Static middleware registered.");
/*-------------------------------*/
export default app;
