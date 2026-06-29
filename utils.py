from django.core.cache import cache
import time

def rate_limit(key, limit=5, period=60):
    """
    Limite les requêtes : 5 tentatives en 60 secondes
    Retourne True si la limite est atteinte
    """
    current_time = time.time()
    requests = cache.get(key, [])
    requests = [t for t in requests if current_time - t < period]
    
    if len(requests) >= limit:
        return True
    
    requests.append(current_time)
    cache.set(key, requests, period)
    return False