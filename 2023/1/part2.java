import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.regex.Pattern;

public class part2 {
    private static Pattern pattern = Pattern.compile("-?\\d+(\\.\\d+)?");
    public static boolean isNumeric(String text)
    {
        if (text == null) {
            return false;
        }
        return pattern.matcher(text).matches();
    }

    public static void main(String[] args) {
        Path path = Paths.get("data.txt");
        try {
            int s = 0;
            List<String> lines = Files.readAllLines(path);
            List<Integer> suma = new ArrayList<Integer>();
            for(String val : lines)
            {
                String newVal = "";
                List<Integer> list = new ArrayList<Integer>();

//                string.forEach((key,value)->{
//                    newVal = val.replace(key,value);
//                });
                newVal = val.replace("one", "o1e").replace("two", "t2o").replace("three", "t3e").replace("four", "f4r").replace("five", "f5e").replace("six", "s6x").replace("seven", "s7n").replace("eight", "e8t").replace("nine", "n9e");
                for(int i  = 0; i < newVal.length(); i++)
                {
                    if(isNumeric(Character.toString(newVal.charAt(i))))
                    {
                        list.add(Character.getNumericValue( newVal.charAt(i)));
                    }
                }
                if(list.size() > 1)
                {
                    String a = list.get(0).toString();
                    String b = list.get(list.size() - 1).toString();
                    suma.add(Integer.parseInt(a+b));
                }
                else
                {
                    String a = list.get(0).toString();
                    String b = list.get(0).toString();
                    suma.add(Integer.parseInt(a+b));
                }

            }

            for(int val: suma)
            {
                s+=val;
            }
            System.out.println(s);
        }
        catch (IOException ex)
        {
            System.out.println(ex);
        }
    }
}
