# listview를 scrollview로 만들기

## <li> setFillViewport
    void setFillViewport (boolean fillViewport)

    android:fillViewport = "True"


ScrollView를 사용하면 안쪽에 있는 Layout이 wrap_content의 형태로 들어간다. 하지만 ScrollView의 안쪽 layout이 match_parent의 형태가 되어 스크롤 뷰에 꽉 차게 하려면 fillViewPort값을 True로 변경해 contents를 view port의 사이즈로 변경한다.

# <li> xml코드 예시
    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:orientation="vertical"
        android:padding="5dp"
        xmlns:android="http://schemas.android.com/apk/res/android"
        android:weightSum="1">

        <ScrollView
            android:layout_width="match_parent"
            android:layout_height="match_parent"
            android:fillViewport="true" >
        <ListView
            android:id="@+id/listview1"
            android:layout_width="match_parent"
            android:layout_height="match_parent" />
        </ScrollView>
    </LinearLayout>
