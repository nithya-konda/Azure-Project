#we dont directly make scd 2 on the silvder table
#we take tables from silver as source, create a staging table stg and then apply scd2 on that

#expectations are data validity checks so no data corruptted comes to us

#we have 3 choices either to warn and take corrupted data or to fail the job or to drop the records and continue the job
#we can also use the drop records option to drop the records and continue the job
#we can also use the fail job option to fail the job if there is any data corruption
#we can also use the warn option to warn the user if there is any data corruption



import dlt

expectations = {
    "rule_1" : "user_id IS NOT NULL"
}

#this will create a table on the data of the df
#declarative pipeline
@dlt.table
@dlt.expect_all_or_drop(expectations)
def dimuser_stg():
    df = spark.readStream.table("spotify_cata.silver.dimuser")
    return df

dlt.create_streaming_table("dimuser")


#Here the scd2 works on sequence by column
#If a record is updated the updated_at value changes and new record is inserted in this scemario
dlt.create_auto_cdc_flow(
    target = "dimuser",
    source = "dimuser_stg",
    keys = ["user_id"],
    sequence_by = "updated_at",
    stored_as_scd_type = 2,
    track_history_except_column_list = None,
    name = None,
    once = False
)