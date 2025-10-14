 /* subqueries up a gear! You only have time to 
--- watch so much soccer, and want to know if the England Premier 
 ---League is exciting as people say.

You'll compare the maximum number of goals scored in a single match 
across each season against the maximum for the England Premier League*/



SELECT 
    season,
    MAX(home_goal + away_goal) AS max_goals,
    (SELECT MAX(home_goal + away_goal) 
     FROM match 
     WHERE season = main.season
     -- Subquery to get the max goals in a Premier League match for the same season
     AND country_id IN (SELECT country_id FROM league WHERE name ='England Premier League')
    ) AS pl_max_goals
FROM match AS main
GROUP BY season;