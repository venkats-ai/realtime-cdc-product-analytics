# realtime-cdc-product-analytics
New Repo
# Real-time CDC Product Analytics (Snowflake + Streams + Tasks)

## Business Problem
SaaS products lose users silently due to lack of real-time visibility into user activity and engagement. This project builds a real-time analytics pipeline to track events, daily active users (DAU), feature usage, and engagement trends.

## Architecture (v1)
- Raw events (JSON) → transformed into structured rows
- Loaded into Snowflake RAW layer (`RAW.EVENTS_RAW`)
- Snowflake Streams + Tasks propagate new events into:
  - `ANALYTICS.FACT_EVENTS`
  - `ANALYTICS.FACT_DAILY_PRODUCT_METRICS`

## Current Status
- Snowflake schemas and tasks defined
- Local Python ETL prototype implemented (`glue/glue_job.py`)
- Next step: Move ETL logic into AWS Glue job and connect to real Snowflake instance
