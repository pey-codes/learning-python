-- Query 1: how many rows are in the table?
SELECT COUNT(*) FROM train;


-- Query 2: how many songs have Popularity above 80?
SELECT COUNT(*) FROM train WHERE Popularity > 80;


-- Query 3: highest Popularity
SELECT MAX(Popularity) FROM train;


-- Query 4: top 5 songs by Popularity (track name and popularity)
SELECT "Track Name", Popularity FROM train ORDER BY Popularity DESC LIMIT 5;


-- Query 5: how many different artists?
SELECT COUNT(DISTINCT "Artist Name") FROM train;


-- Query 6: average Popularity
SELECT AVG(Popularity) FROM train;


-- Query 7: top 5 artists by number of songs
SELECT "Artist Name", COUNT(*) AS song_count FROM train GROUP BY "Artist Name" ORDER BY song_count DESC LIMIT 5;


-- Query 8: artists with more than 40 songs?
SELECT "Artist Name", COUNT(*) AS song_count FROM train GROUP BY "Artist Name" HAVING COUNT(*) > 40 ORDER BY song_count DESC;


-- Query 9: all songs by Britney Spears
SELECT "Track Name" FROM train WHERE "Artist Name" = 'Britney Spears';


-- Query 10: which songs are both very popular and very danceable?
SELECT "Track Name", Popularity FROM train WHERE Popularity > 80 AND danceability > 0.8;
-- Finding: Only 60 out of 17,996 songs are both very popular (above 80) and very danceable (above 0.8), including Passionfruit and Shape of You.
