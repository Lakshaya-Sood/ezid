import db from ".";

const Readings = db.model(
  "Readings",
  {
    uii: String,
    timestamp: Date,
    scannerid: String
  },
  "readings"
);

export default Readings;
