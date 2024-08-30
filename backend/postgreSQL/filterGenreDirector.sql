
CREATE OR REPLACE FUNCTION get_movie_by_id(movie_id_inpute int)
RETURNS TABLE (
    movie_id BIGINT,
    title VARCHAR(100),
    description TEXT,
    director_name VARCHAR(100),
    genre_name VARCHAR(100),
    duration INT,
    now_playing BOOLEAN,
    featured_image VARCHAR -- Add this line to include the image field
) AS $$
BEGIN
    RETURN QUERY
    SELECT 
        m.id AS movie_id,
        m.title,
        m.description,
        d.name AS director_name,
        g.name AS genre_name,
        m.duration,
        m.now_playing,
        m.featured_image -- Include the image field in the SELECT statement
    FROM 
        "cinemaApi_movie" m
    JOIN 
        "cinemaApi_director" d ON m.director_id = d.id
    JOIN 
        "cinemaApi_genre" g ON m.genre_id = g.id
    WHERE
		m.id = movie_id_inpute;
  	IF NOT FOUND THEN
    	RAISE EXCEPTION 'Movie with ID % not found', movie_id_input;
	end if;
END;
$$ LANGUAGE plpgsql;

