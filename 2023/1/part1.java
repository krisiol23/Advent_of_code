import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.io.IOException;
import java.util.regex.Pattern;

public class part1 {
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
                List<Integer> list = new ArrayList<Integer>();
                for(int i  = 0; i < val.length(); i++)
                {
                    if(isNumeric(Character.toString(val.charAt(i))))
                    {
                        list.add(Character.getNumericValue( val.charAt(i)));
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
