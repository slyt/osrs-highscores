import threading
import helpers

helpers.default_skills


if __name__ == "__main__":
  
    # creating threads
    skill_list = list(helpers.default_skills.keys())[1:]
    print(skill_list)
    
    thread_list = []
    for skill in skill_list:
        thread_list.append(threading.Thread(target=helpers.binary_search, name=skill, args=(skill,)))

  
    # starting threads
    for thread in thread_list:
        thread.start()

    # wait until all threads finish
    for thread in thread_list:
        thread.join()