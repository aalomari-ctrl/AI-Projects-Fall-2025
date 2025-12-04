import os
import numpy as np
import threading as th

class myThread(th.Thread):
   def __init__(self, name, threadID, chunk):
      th.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.chunk = chunk
   def run(self):
      print("Starting " + self.name)
      extract_xy(self.name, self.chunk)

def extract_xy(threadName, list_videos):
    relative_flow_dataset_directory = "Data/Crowd-11/flow/"
    flowvideos = os.listdir(relative_flow_dataset_directory)

    total_videos = len(flowvideos)
    completed_videos = 0

    for video_name in list_videos:
        
        # Load the optical flow data from the .npy file
        flow = np.load(os.path.join(relative_flow_dataset_directory, video_name))

        # Separate the x and y components
        x_components = flow[:, :, :, 0]
        y_components = flow[:, :, :, 1]

        # Save the x and y components with appropriate filenames
        np.save(f'{video_name}_x.npy', x_components)
        np.save(f'{video_name}_y.npy', y_components)

        completed_videos += 1

        # Calculate progress percentage
        progress_percentage = (completed_videos / total_videos) * 100
        
        # Display the progress bar and progress percentage in the console
        print(f'\r[{">" * int(progress_percentage / 2)}{" " * (50 - int(progress_percentage / 2))}] {progress_percentage:.2f}%', end="")
        
    print("\nX and Y components have been saved for all videos.")

def chunkIt(seq, num):
   """
   Split a list into num parts
   :param seq: The list to split
   :param num: Number of parts to split
   :return: A list of num sublists
   """
   avg = len(seq) / float(num)
   out = []
   last = 0.0

   while last < len(seq):
      out.append(seq[int(last):int(last + avg)])
      last += avg

   return out

if __name__ == '__main__':
   os.chdir('../')
   crowd11_folder = 'Data/Crowd-11/flow'
   crowd11_of_folder = 'Data/Crowd11_OpticalFlow/'
   list_videos = os.listdir(crowd11_folder)
   nb_threads = 10

   chunks_videos = chunkIt(list_videos, nb_threads)

   threads = []
   for num_thread in range(0, nb_threads):
      # Create new thread
      thread = myThread("Thread-"+str(num_thread), num_thread, chunks_videos[num_thread])
      # Start new Thread
      thread.start()
      # Add thread to thread list
      threads.append(thread)

   # Wait for all threads to complete
   for thread in threads:
      thread.join()
   print("Exiting main thread")
