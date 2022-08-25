/* Write your T-SQL query statement below */
select a.player_id,a.device_id from Activity a join (select player_id,min(event_date) as event_date from Activity group by player_id)b
on a.player_id=b.player_id and a.event_date=b.event_date