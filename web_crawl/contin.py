def continue_crawl(search_history, target_url, max_steps=25):
    if len(search_history) > max_steps:
        print("The search has gone on suspiciously long, aborting search!")
        return False
    elif search_history[-1] == target_url:
        print("We've found the target article!")
        return False
    elif search_history[-1] in search_history[:-1]:
        print("We've arrived at the article we've already seen: {}".format(search_history[-1]))
        return False
    else:
        return True
