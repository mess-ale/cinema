CREATE OR REPLACE FUNCTION get_movie_by_id(movie_id_input BIGINT)
RETURNS TABLE (
    movie_id BIGINT,
    title VARCHAR(100),
    description TEXT,
    director_name VARCHAR(100),
    genre_name VARCHAR(100),
    duration INT,
    now_playing BOOLEAN,
    featured_image VARCHAR
) AS $$
BEGIN
  RETURN QUERY
  SELECT 
    c.id AS movie_id,
    c.title,
    c.description,
    c.director_id,
    c.genre_id,
    c.duration,
    c.now_playing,
    c.featured_image
  FROM 
    "cinemaApi_movie" c
  WHERE 
    c.id = movie_id_input;

  IF NOT FOUND THEN
    RAISE EXCEPTION 'Movie with ID % not found', movie_id_input;
  END IF;
END;
$$ LANGUAGE plpgsql;

SELECT * FROM get_movie_by_id(1);
