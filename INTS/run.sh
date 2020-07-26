#!/bin/bash
cd /Users/joshuagt/Documents/PycharmProjects/LINEToday\ Scraper

for ((i=0; i<=1000; i++)); do
  sleep 1h
  scrapy crawl linetoday -o results_linetoday.csv
  sleep 10s
  scrapy crawl detik -o results_detik.csv
  sleep 10s
  scrapy crawl antara -o results_antara.csv
  sleep 3600s
  done
