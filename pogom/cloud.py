from pogom.utils import get_args
from .utils import get_pokemon_name
from datetime import datetime

from gcloud import datastore

args = get_args()
client = datastore.Client(args.gds_key)


def logPokemon(eid,spid,pid,lat,lng,itime,lured):

    with client.transaction():
        incomplete_key = client.key('Pokemon')

        task = datastore.Entity(key=incomplete_key)
        pokemon_name = get_pokemon_name(id).lower()
        pokemon_id = str(pid)

        task.update({
            'encounterid': eid,
            'spawnid': spid,
            'pokemonid': pokemon_id,
            'name': pokemon_name.encode('utf-8'),
            'latitude': lat,
            'longitude': lng,
            'expired': itime,
            'found': datetime.now(),
            'lured': lured
        })

        client.put(task)
    # [END insert]

    return task
