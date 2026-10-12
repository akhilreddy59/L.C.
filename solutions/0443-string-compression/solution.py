class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        read =0
        write = 0

        while read < len(chars):
            currentChars = chars[read]
            count = 0

            while read < len(chars) and chars[read] == currentChars:
                read += 1
                count += 1

            chars[write] = currentChars
            write +=1

            if count > 1:
                countStr = str(count)
                for i in countStr:
                    chars[write] = i
                    write +=1
        
        return write

        
