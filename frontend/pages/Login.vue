<template>
    <Cover text="Log in/Register" />
    <div class="flex text-black justify-center items-center pt-3 pb-12">
        <div class="bg-white rounded-lg w-full max-w-md">
            <div class="flex justify-center mb-4 text-primary">
                <div @click="setTab('login')" :class="tabClass('login')" class="cursor-pointer px-4 py-2">
                    Login
                </div>
                <div @click="setTab('register')" :class="tabClass('register')" class="cursor-pointer px-4 py-2">
                    Register
                </div>
            </div>
            <form @submit.prevent="handleSubmit">
                <div v-if="currentTab === 'login'">
                    <!-- Login Form -->
                    <div class="mb-4">
                        <label for="username" class="block text-gray-700 font-medium mb-2">Username or email
                            address</label>
                        <input id="username" v-model="username" type="text"
                            class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:border-blue-500"
                            required />
                    </div>
                    <div class="mb-4 relative">
                        <label for="password" class="block text-gray-700 font-medium mb-2">Password</label>
                        <input id="password" v-model="password" :type="passwordVisible ? 'text' : 'password'"
                            class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:border-blue-500"
                            required />
                        <span @click="togglePasswordVisibility"
                            class="absolute right-3 top-1/2 transform -translate-y-1/2 cursor-pointer flex items-center justify-center">
                            <!-- SVG Icons for Password Toggle -->
                            <svg v-if="passwordVisible" xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-gray-500"
                                viewBox="0 0 20 20" fill="currentColor">
                                <path
                                    d="M10 4.5c-3.333 0-6.18 1.737-8.538 4.879a1.5 1.5 0 000 1.742C3.82 14.763 6.667 16.5 10 16.5s6.18-1.737 8.538-4.879a1.5 1.5 0 000-1.742C16.18 6.237 13.333 4.5 10 4.5zM10 15a4.5 4.5 0 110-9 4.5 4.5 0 010 9zm0-2a2.5 2.5 0 100-5 2.5 2.5 0 000 5z" />
                            </svg>
                            <svg v-else xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-gray-500"
                                viewBox="0 0 20 20" fill="currentColor">
                                <path
                                    d="M2.454 7.06a1.5 1.5 0 012.121-2.121l1.36 1.36A7.97 7.97 0 0110 4.5c3.333 0 6.18 1.737 8.538 4.879a1.5 1.5 0 010 1.742 8.08 8.08 0 01-1.682 1.94l1.393 1.393a1.5 1.5 0 01-2.121 2.121L2.454 7.06zm6.03 6.03l2.615 2.614c-.347.106-.709.197-1.099.197a4.5 4.5 0 01-4.5-4.5c0-.39.091-.752.197-1.1l2.615 2.614z" />
                            </svg>
                        </span>
                    </div>
                    <div class="mb-4 flex items-center">
                        <input type="checkbox" id="rememberMe" v-model="rememberMe" class="mr-2" />
                        <label for="rememberMe" class="text-gray-700">Remember me</label>
                    </div>
                    <div class="mb-4">
                        <button type="submit" class="w-full bg-primary text-white py-2 rounded-md">Log in</button>
                    </div>
                    <div class="text-center">
                        <a href="#" class="text-blue-500 hover:underline">Lost your password?</a>
                    </div>
                </div>

                <div v-if="currentTab === 'register'">
                    <!-- Registration Form -->
                    <div class="mb-4">
                        <label for="reg-username" class="block text-gray-700 font-medium mb-2">Username</label>
                        <input id="reg-username" v-model="regUsername" type="text"
                            class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:border-blue-500"
                            required />
                    </div>
                    <div class="mb-4">
                        <label for="reg-email" class="block text-gray-700 font-medium mb-2">Email address</label>
                        <input id="reg-email" v-model="regEmail" type="email"
                            class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:border-blue-500"
                            required />
                    </div>
                    <div class="mb-4 relative">
                        <label for="reg-password" class="block text-gray-700 font-medium mb-2">Password</label>
                        <input id="reg-password" v-model="regPassword" :type="regPasswordVisible ? 'text' : 'password'"
                            class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:border-blue-500"
                            required />
                        <span @click="toggleRegPasswordVisibility"
                            class="absolute right-3 top-1/2 transform -translate-y-1/2 cursor-pointer">
                            <!-- SVG Icons for Password Toggle -->
                            <svg v-if="regPasswordVisible" xmlns="http://www.w3.org/2000/svg"
                                class="h-5 w-5 text-gray-500" viewBox="0 0 20 20" fill="currentColor">
                                <path
                                    d="M10 4.5c-3.333 0-6.18 1.737-8.538 4.879a1.5 1.5 0 000 1.742C3.82 14.763 6.667 16.5 10 16.5s6.18-1.737 8.538-4.879a1.5 1.5 0 000-1.742C16.18 6.237 13.333 4.5 10 4.5zM10 15a4.5 4.5 0 110-9 4.5 4.5 0 010 9zm0-2a2.5 2.5 0 100-5 2.5 2.5 0 000 5z" />
                            </svg>
                            <svg v-else xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-gray-500"
                                viewBox="0 0 20 20" fill="currentColor">
                                <path
                                    d="M2.454 7.06a1.5 1.5 0 012.121-2.121l1.36 1.36A7.97 7.97 0 0110 4.5c3.333 0 6.18 1.737 8.538 4.879a1.5 1.5 0 010 1.742 8.08 8.08 0 01-1.682 1.94l1.393 1.393a1.5 1.5 0 01-2.121 2.121L2.454 7.06zm6.03 6.03l2.615 2.614c-.347.106-.709.197-1.099.197a4.5 4.5 0 01-4.5-4.5c0-.39.091-.752.197-1.1l2.615 2.614z" />
                            </svg>
                        </span>
                    </div>
                    <div class="mb-4">
                        <button type="submit" class="w-full bg-primary text-white py-2 rounded-md">Register</button>
                    </div>
                </div>
            </form>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            currentTab: 'login',
            username: '',
            password: '',
            rememberMe: false,
            passwordVisible: false,
            regUsername: '',
            regEmail: '',
            regPassword: '',
            regPasswordVisible: false,
        };
    },
    methods: {
        setTab(tab) {
            this.currentTab = tab;
        },
        tabClass(tab) {
            return this.currentTab === tab ? 'font-bold' : '';
        },
        togglePasswordVisibility() {
            this.passwordVisible = !this.passwordVisible;
        },
        toggleRegPasswordVisibility() {
            this.regPasswordVisible = !this.regPasswordVisible;
        },
        async handleSubmit() {
            try {
                let response;
                if (this.currentTab === 'login') {
                    response = await this.$axios.post('/api/user/login/', {
                        username: this.username,
                        password: this.password,
                        rememberMe: this.rememberMe,
                    });
                } else if (this.currentTab === 'register') {
                    response = await this.$axios.post('/api/user/register/', {
                        username: this.regUsername,
                        email: this.regEmail,
                        password: this.regPassword,
                    });
                }

                
                if (response.data && response.data.token) {
                    
                    console.log('Success:', response.data);
                } else {
                    // Handle API error
                    console.error('Error:', response.data.message);
                }
            } catch (error) {
                console.error('Error:', error.response ? error.response.data.message : error.message);
            }
        },
    },
};
</script>