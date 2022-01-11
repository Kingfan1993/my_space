package creational_pattern.singleton_pattern;

import java.util.Objects;

/**
 * 单例模式核心: 构造方法私有化、 提供统一获取对象的方法
 *
 * 简单单例模式
 */
public class Singleton {

    // 统一的静态变量
    private static Singleton singleton;

    /**
     * 构造方法私有化
     */
    private Singleton(){}

    /**
     * 构建统一的获取对象的入口
     *
     * @return
     */
    private static Singleton getInstance(){
        if (null == singleton){
            singleton = new Singleton();
            return singleton;
        }
        return singleton;
    }

    public static void main(String[] args) {
        Singleton obj1 = Singleton.getInstance();
        Singleton obj2 = Singleton.getInstance();
        boolean equals = Objects.equals(obj1, obj2);
        System.out.println(equals);
    }
}

