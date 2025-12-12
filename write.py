
#  read the file and store all the lines  in list
#reverse the list and write the reversed lines to new file


with open('text.txt','w') as reader:

      content = reader.readlines() # ['ahfjcd\n', 'bbhfhuh\n', 'cffcb\n', 'defy\n', 'f7y']
      reversed(content) #[ahfjcd bbhfhuh cffcb defy f7y]
with open('test.txt','w') as writer:
      for line in reversed(content):
          writer.write(line)



reader.close()
