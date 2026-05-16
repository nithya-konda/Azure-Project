#we dont directly make scd 2 on the silvder table
#we take tables from silver as source, create a staging table stg and then apply scd2 on that

import dlt


#this will create a table on the data of the df
#declarative pipeline
@dlt.table
def dimartist_stg():
    df = spark.readStream.table("spotify_cata.silver.dimartist")
    return df

dlt.create_streaming_table("dimartist")


#Here the scd2 works on sequence by column
#If a record is updated the updated_at value changes and new record is inserted in this scemario
dlt.create_auto_cdc_flow(
    target = "dimartist",
    source = "dimartist_stg",
    keys = ["artist_id"],
    sequence_by = "updated_at",
    stored_as_scd_type = 2,
    track_history_except_column_list = None,
    name = None,
    once = False
)