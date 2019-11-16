import db from ".";

const Locations = db.model(
  "Locations",
  {
    scannerid: String,
    name: String,
    description: String,
    geometry: {
      type: String,
      coordinates: [String]
    }
  },
  "locations"
);

export default Locations;
