class StorageFilters(object):    
    
    def filter_url(self, url=None):
        """Returns a filter function to filter hits by url.
        """
        def filter_function(item):
            """Filter hits by url. Return false if item doesn't match the given
            url, true otherwise.
            """
            if url is not None:
                if item['url'] != url:
                    return False
            return True
        return filter_function

    def filter_timestamp(self, start_time=None, end_time=None):
        """Return a filter function for filtering by start and end time.
        """
        def filter_function(item):
            """Filter hits by start and end time.
            Returns false if out of bounds, true otherwise.
            """
            if start_time is not None:
                if item['timestamp'] < start_time:
                    return False
            if end_time is not None:
                if item['timestamp'] > end_time:
                    return False
            return True
        return filter_function

    def filter_hitcount(self, minimum_hits=None, maximum_hits=None):
        """Returns a filter function for filtering by minimum and maximum hits.
        """
        def filter_function((url, count),):
            """Filter hitcounts by minimum or maximum number of hits.
            Returns false if out of bounds, true otherwise.
            """
            if minimum_hits is not None:
                if count < minimum_hits:
                    return False
            if maximum_hits is not None:
                if count > maximum_hits:
                    return False
            return True
        return filter_function

    def filter_keywordcount(self, minimum_count=None):
        """Returns a filter function for filtering by minimum keyword count.
        """
        def filter_function((keyword, count),):
            """Filter keywords by minimum count.
            Returns false if count is less than minimum_count, true otherwise.
            """
            if minimum_count is not None:
                if count < minimum_count:
                    return False
            return True
        return filter_function

    def filter_path(self, path):
        """Returns a filter function for filtering incoming hits by a blacklist.
        """
        blacklist = ['','/','/index.php']
        if path in blacklist:
            return False
        return True 
