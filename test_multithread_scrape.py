import threading
import helpers

helpers.default_skills


if __name__ == "__main__":
  
    # creating threads
    t1 = threading.Thread(target=helpers.binary_search, name='defence', args=('defence',))
    t2 = threading.Thread(target=helpers.binary_search, name='attack', args=('attack',))  
  
    # starting threads
    t1.start()
    t2.start()
  
    # wait until all threads finish
    t1.join()
    t2.join()