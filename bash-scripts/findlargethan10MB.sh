#!/bin/bash
find $1  -type f -size +10M -print0 |xargs -0 du -h|sort -nr
