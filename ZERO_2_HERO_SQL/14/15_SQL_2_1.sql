/*The OVER() clause allows you to apply an aggregate function across a dataset, similar to subqueries in SELECT. 
The OVER() clause offers significant benefits over subqueries in SELECT -- namely, your queries will run faster, and
 the OVER() clause has a wide range of additional functions and clauses you can include with it which we will cover 
 later in this chapter.

In this exercise, you will revise some queries from previous chapters using the OVER() clause.

Instructions:->
Select the match ID, country name, season, home, and away goals from the match and country tables.
Complete the query that calculates the average number of goals scored overall and then includes the aggregate value
 in each row using a window function.
*/
SELECT 
	-- Select the id, country name, season, home, and away goals
	m.id, 
    c.name AS country, 
    m.season,
	m.home_goal,
	m.away_goal,
    -- Use a window to include the aggregate average in each row
	AVG(m.home_goal + m.away_goal) OVER() AS overall_avg
FROM match AS m
LEFT JOIN country AS c ON m.country_id = c.id;
