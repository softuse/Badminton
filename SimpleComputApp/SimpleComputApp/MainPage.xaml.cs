using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Xamarin.Forms;

namespace SimpleComputApp
{
    public partial class MainPage : ContentPage
    {
        public MainPage()
        {
            InitializeComponent();
        }
        private void PressMeButton_Pressed(object sender, EventArgs e)
        {
            (sender as Button).Text = "You pressed me!";
        }

        private void PressMeButton_Clicked(object sender, EventArgs e)
        {
            //(sender as Button).Text = "I was just clicked!";
            if (string.IsNullOrEmpty(siteusefee.Text) || string.IsNullOrEmpty(ballfee.Text) || (string.IsNullOrEmpty(twoHoursPeopleNum.Text) && string.IsNullOrEmpty(oneHoursPeopleNum.Text)))
            {
                DisplayAlert("提示", "请填写数值", "cancel");

                return;
            }
            int t1, t2, t3 = 0, z5 = 0;
            if (int.TryParse(siteusefee.Text, out t1) && int.TryParse(ballfee.Text, out t2) && (int.TryParse(twoHoursPeopleNum.Text, out t3) || int.TryParse(oneHoursPeopleNum.Text, out z5)))
            {
                var tmp = Math.Round((decimal)(t1 + t2) / (t3 * 2 + z5), 2);
                // double tmp1 = (t1 + t2) / (t3 * 2 + z5);
                var model = (t1 + t2) % (t3 * 2 + z5);
                int ave = model == 0 ? (int)tmp : ((int.Parse(tmp.ToString().Substring(tmp.ToString().IndexOf('.') + 1, 1))) > 0 ? (int)tmp + 1 : (int)tmp);// 人均 
                var tmp2 = tmp * 2;
                int twoHoursPrice = model == 0 ? (int)tmp2 : ((int.Parse((tmp2).ToString().Substring(tmp2.ToString().IndexOf('.') + 1, 1))) > 0 ? (int)tmp2 + 1 : (int)tmp2);//
                string s = z5 != 0 ? $"今日场地费{t1}，球费{t2}，人数{t3 + z5}，人均{twoHoursPrice}，其中            一小时，收{ave}元。" : $"今日场地费{t1}，球费{t2}，人数{t3 + z5}，人均{twoHoursPrice}";
                rich.Text = s;
            }
            else
            {
                DisplayAlert("提示", "请填写数值", "cancel");
                return;
            }
        }
    }
}
