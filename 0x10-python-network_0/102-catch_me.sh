#!/bin/bash
#Script that returns body
curl -sL -XPUT -d user_id=98 -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me
