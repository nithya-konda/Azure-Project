#we dont directly make scd 2 on the silvder table
#we take tables from silver as source, create a staging table stg and then apply scd2 on that

import dlt


#this will create a table on the data of the df
#declarative pipeline
@dlt.table
def factstream_stg():
    df = spark.readStream.table("spotify_cata.silver.factstream")
    return df

dlt.create_streaming_table("factstream")


#Here the scd2 works on sequence by column
#If a record is updated the updated_at value changes and new record is inserted in this scemario
dlt.create_auto_cdc_flow(
    target = "factstream",
    source = "factstream_stg",
    keys = ["stream_id"],
    sequence_by = "stream_timestamp",
    stored_as_scd_type = 1,
    track_history_except_column_list = None,
    name = None,
    once = False
)