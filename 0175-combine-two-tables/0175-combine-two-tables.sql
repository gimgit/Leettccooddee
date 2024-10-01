select
    firstname,
    lastname,
    city,
    state
from person as PT
left join address as AT
using (personId)