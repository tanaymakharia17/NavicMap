
import httpService from "./httpService";

import config from "../config/config.json";

const url = config.apiEndPoint;

export function getDir(places) {
    return httpService.post(url, places);
}

export default {
    getDir
}