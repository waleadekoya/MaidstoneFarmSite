-- inventory snapshot
select
       penNumber_id as penNumber,
       specieType_id,
       dateTimeRecorded,
       totalCount,
       comments
from closing_snails_inventory s1
where
      dateTimeRecorded = (
          select
                 max(dateTimeRecorded)
          from closing_snails_inventory s2
          where
                s1.penNumber_id = s2.penNumber_id)
      and totalCount > 0
order by penNumber_id, dateTimeRecorded;

-- activity summary
select
       dateTimeRecorded,
       penNumber_id as penNumber,
       sum(totalMortalities) as mortalities,
       sum(newEggsCollected) as eggsCollected,
       sum(newBabySnails) as babySnails,
       sum(newBreederStocks) as breederStocks
from snails_activities
group by penNumber_id, dateTimeRecorded
having mortalities > 0 or eggsCollected > 0 or babySnails > 0 or breederStocks > 0
order by dateTimeRecorded, penNumber_id;

-- eggs snapshot
select * from eggs_inventory s1
where id = (select max(id) from eggs_inventory s2)