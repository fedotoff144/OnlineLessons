public class Second implements First{
    private String word = "muu";

    public String getWord(){
        return this.word;
    }
    public void setWord(String word){
        this.word = word;
    }

    @Override
    public String outLine() {
        return String.format("this is - " + word);
    }

}
