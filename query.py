# Import the submodule required
from sqlalchemy import func
from base import session
from tables import PprCleanAll
# Get the maximum, minimum and average values for each product category
result = session.query(PprCleanAll.county,
                       func.max(PprCleanAll.price),
                       func.min(PprCleanAll.price),
                       func.avg(PprCleanAll.price)) \
                .group_by(PprCleanAll.county).all()

print("Result:", result[:5])


# Create the view with the appropriate metrics
query = """
CREATE OR REPLACE VIEW insights AS
SELECT county,
       COUNT(*) AS sales_count,
       SUM(CAST(price AS int)) AS sales_total,
       MAX(CAST(price AS int)) AS sales_max,
       MIN(CAST(price AS int)) AS sales_min,
       AVG(CAST(price AS int))::numeric(10,2) AS sales_avg
FROM ppr_clean_all
GROUP BY county
"""

# Execute and commit
session.execute(query)
session.commit()